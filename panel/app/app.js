// Панель направлений. Роутинг на хэшах, без перезагрузки страницы.
// Весь вид — только классами из style.css: своих классов и инлайн-стилей нет.
// innerHTML получает ТОЛЬКО вывод window.mdToHtml — тот экранирует входной текст.

let STATE = null;
// Токен отрисовки: ответ fetch, пришедший после ухода со страницы, не рисуется.
let RENDER_TOKEN = 0;

// Куда вести ссылку на направление: на первый ГОТОВЫЙ раздел. Имя в коде
// означало бы, что закрытие раздела оставляет мёртвую ссылку.
function firstReady(d) {
  const s = (d.sections || []).find((x) => x.ready);
  return "#/" + d.id + "/" + (s ? s.id : "");
}

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

// Узел, содержимое которого — markdown, отрисованный window.mdToHtml.
function mdNode(tag, className, markdown) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  node.innerHTML = window.mdToHtml(markdown);
  return node;
}

// Короткие имена месяцев для полосы сроков: дата показывается человеком (15 авг).
const MONTHS_RU = ["янв", "фев", "мар", "апр", "май", "июн",
                   "июл", "авг", "сен", "окт", "ноя", "дек"];

// Фразу про дни собирает СЕРВЕР и присылает готовой (`serve.days_phrase`):
// здесь она собиралась одной формой на все числа и выдавала «через 21 дней».
// Прошедшая дата — не «просрочено»: красного и оценок здесь нет вообще.
function deadlineDaysText(row) {
  return row.phrase;
}

// Полоса сроков. Список пуст — полосы нет совсем: ни заголовка, ни рамки.
function deadlinesBar(rows) {
  if (!rows || !rows.length) return null;
  const bar = el("div", "deadlines");
  bar.appendChild(el("div", "dl-head", "СРОКИ"));
  const grid = el("div", "dl-grid");
  // Строки уже отсортированы по дате: первая непрошедшая — ближайшая будущая.
  const next = rows.find((r) => !r.past) || null;
  for (const r of rows) {
    let cls = "dl-tile";
    if (r === next) cls += " next";
    if (r.past) cls += " past";
    const tile = el("div", cls);
    const parts = String(r.date).split("-");
    const month = MONTHS_RU[parseInt(parts[1], 10) - 1];
    tile.appendChild(el("div", "dl-date",
      month ? parseInt(parts[2], 10) + " " + month : r.date));
    tile.appendChild(el("div", "dl-days", deadlineDaysText(r)));
    if (r.what) tile.appendChild(el("div", "dl-what", r.what));
    if (r.title) tile.appendChild(el("div", "dl-who", r.title));
    if (r.source) tile.appendChild(el("div", "dl-src", r.source));
    grid.appendChild(tile);
  }
  bar.appendChild(grid);
  bar.appendChild(el("div", "dl-note",
    "Даты — его слова. Панель их не назначает и не двигает."));
  return bar;
}

let ROUTE_EXTRA = null;

function parseHash() {
  const parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  ROUTE_EXTRA = parts[2] || null;
  return { direction: parts[0] || null, section: parts[1] || null };
}

function findDirection(id) {
  return STATE.directions.find((d) => d.id === id) || null;
}

function renderTopbar(route) {
  const dirs = document.getElementById("dirs");
  dirs.textContent = "";
  for (const d of STATE.directions) {
    const link = el("a", d.id === route.direction ? "active" : "", d.id);
    link.href = firstReady(d);
    dirs.appendChild(link);
  }

  const build = document.getElementById("build");
  build.textContent = "";
  const b = STATE.build;
  build.appendChild(document.createTextNode(b.commit + " · не отправлено "));
  const warn = el("span", b.unpushed > 0 ? "warn" : null, String(b.unpushed));
  build.appendChild(warn);
  build.appendChild(document.createTextNode(" · не прочиталось "));
  const bad = el("span", b.unread > 0 ? "bad" : null, String(b.unread));
  build.appendChild(bad);

  // Отставшая копия молча показывает позавчерашний мир — и разделы, и состояние
  // направления. Полоса та же, что у нечитаемого файла: есть — видно, нет — её нет.
  const shown = document.getElementById("stale");
  if (shown) shown.remove();
  if (b.stale) {
    const bar = el("div", "problem", b.stale);
    bar.id = "stale";
    document.body.appendChild(bar);
  }
}

function renderPicker() {
  const nav = document.getElementById("nav");
  nav.textContent = "";
  const content = document.getElementById("content");
  content.textContent = "";
  for (const d of STATE.directions) {
    const row = el("a", "row");
    row.href = firstReady(d);
    row.appendChild(el("div", "status", "СТАВКА · —"));
    row.appendChild(el("div", "title", d.id));
    content.appendChild(row);
  }
}

// Строка чисел сверху раздела: по одному span.num на число. Число null
// пропускается целиком; разделитель «·» живёт внутри того же span.
function renderNumbers(content, numbers) {
  if (!numbers) return;
  const items = [];
  items.push("задачи " + numbers.tasks_done + " из " + numbers.tasks_total);
  if (numbers.tracks_limit != null) {
    items.push("полосы " + numbers.tracks_busy + " из " + numbers.tracks_limit);
  }
  items.push("ждёт тебя " + numbers.waiting_for_you);
  if (numbers.bet_days != null) {
    items.push("ставка идёт " + numbers.bet_days + " дня");
  }
  const box = el("div", "numbers");
  for (let i = 0; i < items.length; i += 1) {
    box.appendChild(el("span", "num", items[i] + (i < items.length - 1 ? " ·" : "")));
  }
  content.appendChild(box);
}

// Кнопка «скопировать запуск»: кладёт launch в буфер, на две секунды
// меняет текст на «скопировано». Нет буфера — падаем с явной ошибкой.
function copyLaunch(button, text) {
  if (!navigator.clipboard || !navigator.clipboard.writeText) {
    throw new Error("буфер обмена недоступен");
  }
  navigator.clipboard.writeText(text).then(() => {
    button.textContent = "скопировано";
    setTimeout(() => {
      button.textContent = "скопировать запуск";
    }, 2000);
  });
}

// Одна строка наряда. isReady — наряд можно запускать; иначе он в «прочих».
function renderOrderRow(container, order, isReady) {
  const row = el("div", "row");
  const track = order.track ? " · " + order.track : "";
  if (isReady) {
    row.appendChild(el("div", "status", "МОЖНО ЗАПУСКАТЬ" + track));
    row.appendChild(el("div", "title", order.title));
  } else {
    const status = order.status == null ? "" : String(order.status).toUpperCase();
    row.appendChild(el("div", "status wait", status + track));
    row.appendChild(el("div", "title dim", order.title));
  }
  if (order.description != null) {
    row.appendChild(mdNode("div", "human", order.description));
  } else {
    row.appendChild(el("div", "human dim", "описания нет"));
  }
  if (order.description_by === "dev") {
    row.appendChild(el(
      "div", "draft",
      "описание составлено при разработке панели, может быть неточным"
    ));
  }
  if (order.why != null) {
    row.appendChild(el("div", "waitline", "ждёт: " + order.why));
  }
  const copyButton = el("button", "act", "скопировать запуск");
  copyButton.addEventListener("click", () => copyLaunch(copyButton, order.launch));
  row.appendChild(copyButton);
  const details = el("div", "details");
  details.hidden = true;
  for (const field of order.fields) {
    // unblock_when уже показан в waitline, description — в human: не повторять.
    if (field.name === "unblock_when" || field.name === "description") continue;
    const item = el("div", "desc");
    item.appendChild(document.createTextNode(field.name + ": "));
    item.appendChild(mdNode("div", null, field.text));
    details.appendChild(item);
  }
  const toggleButton = el("button", "act", "подробности");
  toggleButton.addEventListener("click", () => {
    details.hidden = !details.hidden;
  });
  row.appendChild(toggleButton);
  row.appendChild(details);
  row.appendChild(el("div", "id", order.id));
  container.appendChild(row);
}

// Раздел «Сводка». Вид собран, но из меню всё ещё выключен: включение и замена
// старого контракта ручки принадлежат отдельной задаче. Здесь только read-only
// экран поверх четырёх уже существующих блоков.
const DASH_PREVIEW_LIMIT = 5;

const DASH_NOTE = {
  running: "Если ставки нет, указатель всё равно прочитан: ноль строк остаётся честным нулём.",
  stalled: "Причина остановки пока не показана: это объявленный рез и отдельная работа.",
  done_in_window: "Окно скользящее, а не календарный месяц.",
  problems: "Полный текст открывается по строке; группировка и порядок пока не назначены.",
};

// Текст источника может сам упоминать внутреннюю карточку, путь или коммит.
// Содержание сохраняем, служебные токены вынимаем; пустое всегда имеет одно имя.
function dashboardText(value, fallback) {
  let text = String(value == null ? "" : value);
  text = text.replace(/\b(?:live|panel|os)\/[\w./-]+/gi, " ");
  text = text.replace(/\b[0-9a-f]{7,40}\b/gi, " ");
  // Одиночный латинский status или id направления — тоже машинное имя.
  // В этом экране латиница не является содержанием, поэтому убирается целиком.
  text = text.replace(/\b[a-z][a-z0-9_.-]*\b/gi, " ");
  text = text.replace(/[`*_#]+/g, " ").replace(/\s+/g, " ").trim();
  return text || fallback || "без имени";
}

function dashboardSummary(value, fallback) {
  const text = dashboardText(value, fallback);
  return text.length > 180 ? text.slice(0, 177).trimEnd() + "…" : text;
}

function dashboardRowText(block, row) {
  if (block.id === "done_in_window") {
    const source = row.text || "";
    const colon = source.indexOf(":");
    return dashboardSummary(colon >= 0 ? source.slice(colon + 1) : source, "отчёт ноги");
  }
  if (block.id === "problems") return dashboardSummary(row.text, "проблема без текста");
  return dashboardSummary(row.title, "без имени");
}

function dashboardHref(direction, block, row) {
  const root = "#/" + encodeURIComponent(direction.id) + "/";
  if (row.kind === "node") return root + "goals/" + encodeURIComponent(row.id);
  if (block.id === "done_in_window") return root + "history";
  if (row.kind === "task" || row.kind === "call") return root + "wave";
  return null;
}

function dashboardRow(direction, block, row) {
  const title = dashboardRowText(block, row);
  if (block.id === "problems") {
    const item = el("div", "dash-row dash-record");
    const open = el("button", "dash-row-main", title);
    const body = el("div", "dash-record-body",
      dashboardText(row.body, "полный текст не записан"));
    body.hidden = true;
    open.addEventListener("click", () => { body.hidden = !body.hidden; });
    item.appendChild(open);
    item.appendChild(body);
    return item;
  }
  const href = dashboardHref(direction, block, row);
  const item = el(href ? "a" : "div", "dash-row", title);
  if (href) item.href = href;
  return item;
}

function dashboardActivity(block) {
  const windowInfo = block.window || {};
  const days = Number(windowInfo.days) || 30;
  const counts = {};
  for (const row of block.rows || []) {
    if (row.date) counts[row.date] = (counts[row.date] || 0) + 1;
  }
  const chart = el("div", "dash-activity");
  chart.setAttribute("role", "img");
  chart.setAttribute("aria-label", "Активность ног за скользящие 30 дней");
  const start = new Date(String(windowInfo.start || "") + "T00:00:00Z");
  for (let i = 0; i < days; i += 1) {
    const date = new Date(start.getTime() + i * 86400000).toISOString().slice(0, 10);
    const count = counts[date] || 0;
    const cell = el("span", count ? "dash-day active" : "dash-day");
    cell.setAttribute("title", date + " · ног " + count);
    chart.appendChild(cell);
  }
  return chart;
}

function dashboardBlock(direction, block) {
  const signal = block.id === "running" ? " signal-running"
    : block.id === "stalled" ? " signal-stalled"
      : block.id === "problems" ? " signal-problems" : "";
  const card = el("section", "dash-block" + signal);
  const metric = el("div", "dash-metric");
  metric.appendChild(el("div", "dash-label", dashboardText(block.label, "без имени")));
  metric.appendChild(el("div", "dash-count", String(block.count || 0)));
  // Полный `how` остаётся рядом в HTTP для машинной проверки; `view_how`
  // формируется там же, где считается блок, поэтому экран не заводит вторую методику.
  metric.appendChild(el("div", "dash-how",
    dashboardText(block.view_how, "способ счёта не записан")));
  card.appendChild(metric);

  if (block.id === "done_in_window") {
    card.appendChild(el("div", "dash-chart-label", "АКТИВНОСТЬ · 30 ДНЕЙ"));
    card.appendChild(dashboardActivity(block));
  }

  const rows = block.rows || [];
  const preview = el("div", "dash-preview");
  for (const row of rows.slice(0, DASH_PREVIEW_LIMIT)) {
    preview.appendChild(dashboardRow(direction, block, row));
  }
  if (!rows.length) preview.appendChild(el("div", "dash-zero", "ничего"));
  card.appendChild(preview);

  const more = el("div", "dash-more");
  more.hidden = true;
  for (const row of rows.slice(DASH_PREVIEW_LIMIT)) {
    more.appendChild(dashboardRow(direction, block, row));
  }
  more.appendChild(el("div", block.gap ? "dash-note gap" : "dash-note",
    block.gap ? "Источник этого блока не найден." : DASH_NOTE[block.id]));
  card.appendChild(more);

  const toggle = el("button", "dash-toggle", "подробнее");
  toggle.addEventListener("click", () => {
    more.hidden = !more.hidden;
    toggle.textContent = more.hidden ? "подробнее" : "свернуть";
  });
  card.appendChild(toggle);
  return card;
}

function dayWord(n) {
  const abs = Math.abs(n) % 100;
  const last = abs % 10;
  if (abs > 10 && abs < 20) return n + " дней";
  if (last === 1) return n + " день";
  if (last >= 2 && last <= 4) return n + " дня";
  return n + " дней";
}

function renderDashboard(direction, content) {
  const token = ++RENDER_TOKEN;
  return fetch("/api/section/" + encodeURIComponent(direction.id) + "/dashboard")
    .then((response) => {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const intro = el("div", "dash-intro");
      intro.appendChild(el("div", "dash-name", "без имени"));
      intro.appendChild(el("div", "dash-promise",
        "Что идёт, что стоит, что сделано, какие есть проблемы и что дальше."));
      const age = data.age || {};
      const parts = [];
      if (age.bet_days !== null && age.bet_days !== undefined) {
        parts.push("работа идёт " + dayWord(age.bet_days));
      }
      if (age.quiet_days !== null && age.quiet_days !== undefined) {
        parts.push(age.quiet_days === 0
          ? "последняя нога сегодня"
          : "последняя нога " + dayWord(age.quiet_days) + " назад");
      }
      if (parts.length) {
        const line = el("div", "dash-age", parts.join(" · "));
        line.title = age.how || "";
        intro.appendChild(line);
      }
      content.appendChild(intro);
      const grid = el("div", "dash-grid");
      for (const block of data.blocks || []) grid.appendChild(dashboardBlock(direction, block));
      content.appendChild(grid);
      if (data.unread.length > 0) {
        content.appendChild(el("div", "problem", "НЕ ПРОЧИТАЛОСЬ " + data.unread.length));
      }
    })
    .catch(() => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      content.appendChild(el("div", "problem", "НЕ УДАЛОСЬ ЗАГРУЗИТЬ РАЗДЕЛ"));
    });
}

function taskRow(r) {
  const row = el("div", "row");
  // Чем кончилось — приходит с сервера, а не угадывается по статусу.
  // СДЕЛАНО и СНЯТО — разные вещи; «ЗАКРЫТО» значит, что причину не записали,
  // и этот пробел надо показывать, а не замазывать словом «сделано».
  const WORD = {done: "СДЕЛАНО", dropped: "СНЯТО", closed: "ЗАКРЫТО"};
  const shut = Boolean(r.outcome);
  const st = WORD[r.outcome] || (r.status || "нет статуса").toUpperCase();
  row.appendChild(el("div", r.outcome === "done" ? "status" : (shut ? "status dim" : "status wait"),
    st + (r.order ? " · " + r.order : "")));
  row.appendChild(el("div", shut ? "title dim" : "title", r.goal || r.id));
  if (r.missing) row.appendChild(el("div", "waitline", "карточки нет — полоса называет задачу, которой не существует"));
  if (r.unblock_when) row.appendChild(el("div", "waitline", "ждёт: " + r.unblock_when));
  if (r.done_when) {
    const d = el("div", "desc");
    d.innerHTML = window.mdToHtml("**готово, когда:** " + r.done_when);
    row.appendChild(d);
  }
  row.appendChild(el("div", "id", r.id));
  return row;
}

function goalRow(n, tone, direction) {
  const row = el("div", "goal " + tone);
  row.onclick = () => { location.hash = "#/" + encodeURIComponent(direction.id) + "/goals/" + n.id; };
  row.appendChild(el("div", "goal-name", n.label || n.id));
  const sub = el("div", "goal-hook");
  sub.textContent = (n.hook || "") + (n.hook ? " · " : "") + n.id;
  row.appendChild(sub);
  return row;
}

function goalGroup(content, word, tone, rows, emptyText, direction) {
  const head = el("div", "group " + tone);
  head.textContent = word + " — " + rows.length;
  content.appendChild(head);
  if (!rows.length) {
    content.appendChild(el("div", "group-empty", emptyText || "пусто"));
    return;
  }
  for (const n of rows) content.appendChild(goalRow(n, tone, direction));
}

function renderGoals(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/goals")
    .then((r) => { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";

      const top = el("div", "aim");
      top.appendChild(el("div", "status", "КУДА ИДЁМ"));
      top.appendChild(el("div", "aim-goal", (data.root && data.root.label) || "—"));
      if (data.target) {
        const t = el("div", "aim-date");
        t.appendChild(document.createTextNode("ближайшая дата · "));
        t.appendChild(el("b", null, data.target));
        top.appendChild(t);
      }
      content.appendChild(top);

      const g = data.groups || {};
      goalGroup(content, "ИДЁТ СЕЙЧАС", "now", g.running || [], "ставка не выбрана", direction);
      goalGroup(content, "ДАЛЬШЕ", "ahead", g.ahead || [], null, direction);
      goalGroup(content, "СДЕЛАНО", "done", g.closed_done || [], null, direction);

      const dropped = g.closed_dropped || [];
      if (dropped.length) {
        const d = el("details", "dropped");
        d.appendChild(el("summary", "group gone", "СНЯТО — " + dropped.length));
        for (const n of dropped) d.appendChild(goalRow(n, "gone", direction));
        content.appendChild(d);
      }

      content.appendChild(legendBlock());
      if ((data.no_label || []).length) {
        content.appendChild(el("div", "problem",
          "БЕЗ ИМЕНИ " + data.no_label.length + " — " + data.no_label.join(", ")
          + " · имя пишется при создании цели"));
      }
      if ((data.unread || []).length) {
        content.appendChild(el("div", "problem",
          "НЕ ПРОЧИТАЛОСЬ " + data.unread.length + " — " + data.unread.map((u) => u.file).join(", ")));
      }
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

const LEGEND = [["accent", "идёт сейчас"], ["plan", "впереди · карта"], ["think", "разбор"],
                ["wait", "ждёт тебя"], ["bad", "сломано"], ["done", "сделано"], ["off", "снято"]];

function legendBlock() {
  const lg = el("div", "legend");
  for (const pair of LEGEND) lg.appendChild(el("span", "lg-" + pair[0], "■ " + pair[1]));
  return lg;
}

function firstSentence(t) {
  const i = t.indexOf(". ");
  return (i > 0 ? t.slice(0, i + 1) : t).slice(0, 78);
}

function renderGoalPage(direction, nodeId, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/goal/" + encodeURIComponent(direction.id) + "/" + encodeURIComponent(nodeId))
    .then((r) => { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then((d) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";

      const back = el("div", "back", "← ВСЕ ЦЕЛИ");
      back.onclick = () => { location.hash = "#/" + encodeURIComponent(direction.id) + "/goals"; };
      content.appendChild(back);

      const head = el("div", "head " + d.state);
      const top = el("div", "head-top");
      const tone = d.state === "running" ? "" : (d.state === "ahead" ? " plan" : " gone");
      top.appendChild(el("div", "status" + tone, d.word));
      top.appendChild(el("div", "id", d.id));
      head.appendChild(top);
      head.appendChild(el("div", "head-name", d.label));
      if (d.hook) head.appendChild(el("div", "head-hook", d.hook));
      content.appendChild(head);

      const ev = el("div", "sec");
      ev.appendChild(el("div", "sec-title", "ЧТО БЫЛО — " + d.events.length));
      if (!d.events.length) ev.appendChild(el("div", "group-empty", "событий пока нет"));
      for (const e of d.events) {
        const row = el("div", "ev");
        row.appendChild(el("span", "ev-date", e.date.slice(5).replace("-", ".")));
        row.appendChild(el("span", "ev-kind " + (e.tone || ""), e.kind));
        row.appendChild(el("span", "ev-text", e.text));
        ev.appendChild(row);
      }
      content.appendChild(ev);

      if (d.conditions.length) {
        const cs = el("div", "sec");
        cs.appendChild(el("div", "sec-title", "ЧЕМ ЗАКРЫВАЕТСЯ — " + d.conditions.length + " УСЛОВИЙ"));
        for (const c of d.conditions) {
          const box = el("details", "cond");
          const sum = el("summary");
          sum.appendChild(el("span", "cond-no", String(c.no || "·").padStart(2, "0")));
          const line = el("span");
          if (c.name) line.appendChild(el("span", "cond-name", c.name));
          line.appendChild(el("span", "cond-tail", (c.name ? " — " : "") + firstSentence(c.text)));
          sum.appendChild(line);
          box.appendChild(sum);
          const body = el("div", "cond-body");
          body.innerHTML = window.mdToHtml(c.text);
          box.appendChild(body);
          cs.appendChild(box);
        }
        content.appendChild(cs);
      }

      if (d.why) {
        const w = el("div", "sec");
        w.appendChild(el("div", "sec-title", "ЗАЧЕМ"));
        const x = el("div", "ev-text");
        x.innerHTML = window.mdToHtml(d.why);
        w.appendChild(x);
        content.appendChild(w);
      }

      const ln = el("div", "sec");
      ln.appendChild(el("div", "sec-title", "СВЯЗИ"));
      const jump = (b) => {
        const node = el("b", null, b.label);
        node.onclick = () => { location.hash = "#/" + encodeURIComponent(direction.id) + "/goals/" + b.id; };
        return node;
      };
      if (d.parent) {
        const r = el("div", "link");
        r.appendChild(document.createTextNode("родитель · "));
        r.appendChild(jump(d.parent));
        ln.appendChild(r);
      }
      for (const k of d.children) {
        const r = el("div", "link");
        r.appendChild(document.createTextNode("вобрал · "));
        if (k.dropped) { const st = el("s"); st.appendChild(jump(k)); r.appendChild(st); }
        else { r.appendChild(jump(k)); }
        ln.appendChild(r);
      }
      if (d.detail) ln.appendChild(el("div", "id", d.detail));
      content.appendChild(ln);

      content.appendChild(legendBlock());
    })
    .catch((e) => {
      content.textContent = "";
      content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e));
    });
}

function renderWave(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/wave")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const n = data.numbers || {};
      const nums = el("div", "numbers");
      nums.appendChild(el("span", "num", "задачи " + n.tasks_done + " из " + n.tasks_total));
      if (n.tasks_dropped) nums.appendChild(el("span", "num dim", "снято " + n.tasks_dropped));
      if (n.tasks_closed_unnamed) nums.appendChild(el("span", "num wait",
        "закрыто без причины " + n.tasks_closed_unnamed));
      nums.appendChild(el("span", "num", "полосы " + n.tracks_total + " из " + n.tracks_limit));
      content.appendChild(nums);

      if (data.bet) {
        const b = el("div", "row");
        b.appendChild(el("div", "status", "СТАВКА · " + data.bet.id));
        if (data.bet.goal) b.appendChild(el("div", "title", data.bet.goal));
        if (data.bet.description) {
          const h = el("div", "human");
          h.innerHTML = window.mdToHtml(data.bet.description);
          b.appendChild(h);
        }
        if (data.bet.description_by === "dev") {
          b.appendChild(el("div", "draft", "описание составлено при разработке панели, может быть неточным"));
        }
        if (data.bet.opened) b.appendChild(el("div", "id", "открыта " + data.bet.opened));
        content.appendChild(b);
      }

      for (const t of data.tracks) {
        const head = el("div", "row");
        head.appendChild(el("div", t.done === t.total && t.total > 0 ? "status" : "status wait",
          "ПОЛОСА · " + t.id + " · " + t.done + " из " + t.total));
        if (t.label) head.appendChild(el("div", "title dim", t.label));
        if (t.note) head.appendChild(el("div", "desc", t.note));
        content.appendChild(head);
        for (const r of t.tasks) content.appendChild(taskRow(r));
      }

      if (data.loose && data.loose.length) {
        const h = el("div", "row");
        h.appendChild(el("div", "status bad", "ВНЕ ПОЛОС · " + data.loose.length));
        h.appendChild(el("div", "desc", "эти задачи не названы ни одной полосой"));
        content.appendChild(h);
        for (const r of data.loose) content.appendChild(taskRow(r));
      }

      if (data.unread && data.unread.length) {
        content.appendChild(el("div", "problem",
          "НЕ ПРОЧИТАЛОСЬ " + data.unread.length + " — " + data.unread.map((u) => u.file).join(", ")));
      }
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

// Раздел «ЖДЁТ ТЕБЯ»: только то, где отвечает владелец. Слова групп приходят
// с сервера ключом; вид — только классами из style.css.
const WAITING_WORD = {decision: "РЕШЕНИЕ", question: "ВОПРОС", owner_call: "НАРЯД К ТЕБЕ",
  stalled: "СТОИТ", unnamed_goal: "ЦЕЛЬ БЕЗ ИМЕНИ", closed_unnamed: "ЗАКРЫТО БЕЗ ПРИЧИНЫ"};

function waitingRow(r) {
  const row = el("div", "row");
  row.appendChild(el("div", r.blocking ? "status" : "status wait",
    WAITING_WORD[r.group] || r.group));
  row.appendChild(el("div", r.blocking ? "title" : "title dim", r.title));
  if (r.detail) {
    row.appendChild(mdNode("div", "desc", r.detail));
  }
  if (r.unblock) {
    row.appendChild(el("div", "waitline", "ждёт: " + r.unblock));
  }
  row.appendChild(el("div", "id", r.id));
  return row;
}

function renderWaiting(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/waiting")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const blocking = data.blocking || [];
      const other = data.other || [];
      const counts = {};
      for (const r of blocking.concat(other)) counts[r.group] = (counts[r.group] || 0) + 1;
      const WAITING_COUNTS = [["ждёт ответа", ["decision", "question", "owner_call"]],
        ["стоит", ["stalled"]], ["нужно имя", ["unnamed_goal"]], ["закрыто без причины", ["closed_unnamed"]]];
      const nums = el("div", "numbers");
      for (const [word, groups] of WAITING_COUNTS) {
        const n = groups.reduce((s, g) => s + (counts[g] || 0), 0);
        if (n) nums.appendChild(el("span", "num", word + " " + n));
      }
      if (nums.childNodes.length) content.appendChild(nums);

      if (!blocking.length && !other.length) {
        content.appendChild(el("div", "empty", "НИЧЕГО НЕ ЖДЁТ"));
      }
      for (const r of blocking) content.appendChild(waitingRow(r));
      for (const r of other) content.appendChild(waitingRow(r));

      // Записи ждут события, а не даты — в списках им не место, но число честно показываем.
      if (data.issues_parked > 0) {
        content.appendChild(el("div", "desc",
          data.issues_parked + " записей ждут своего события, дат у них нет"));
      }
      if ((data.unread || []).length) {
        content.appendChild(el("div", "problem",
          "НЕ ПРОЧИТАЛОСЬ " + data.unread.length + " — " + data.unread.map((u) => u.file).join(", ")));
      }
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

// Раздел «ИДЕИ»: отложенное содержание. Ничего не оценивается и не
// сортируется по важности; главное свойство строки — видно, ЧЬЯ это идея.
function ideaRowView(r) {
  const row = el("div", "row");
  if (r.text) row.appendChild(mdNode("div", "human", r.text));
  // Цитата владельца — отдельно от пересказа: его слова не имеют права
  // выглядеть как выдумка ноги.
  if (r.his_words) row.appendChild(el("div", "quote", r.his_words));
  if (r.from === "владелец") {
    row.appendChild(el("div", "desc", "его слова"));
  } else if (r.from === "нога") {
    row.appendChild(el("div", "desc", "придумала нога"));
  } else if (r.from) {
    row.appendChild(el("div", "desc", r.from));
  } else {
    row.appendChild(el("div", "desc dim", "автор не записан"));
  }
  if (r.opened) row.appendChild(el("div", "id", r.opened));
  if (r.source) row.appendChild(el("div", "id", r.source));
  row.appendChild(el("div", "id", r.id));
  return row;
}

function renderIdeas(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/ideas")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const sub = el("div", "row");
      sub.appendChild(el("div", "desc", "Отложенное содержание. Ничего из этого не является требованием."));
      content.appendChild(sub);
      if (!data.count) {
        content.appendChild(el("div", "empty",
          "Пока ни одной. Захват ног живёт в отчётах — перенос оттуда отдельная работа."));
        return;
      }
      for (const g of data.groups || []) {
        const head = el("div", "group");
        head.textContent = g.label + " — " + g.rows.length;
        content.appendChild(head);
        for (const r of g.rows) content.appendChild(ideaRowView(r));
      }
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

// Раздел «ИСТОРИЯ»: по дням, что делали ноги и чем это кончилось. Строка —
// сообщение коммита; чего в источниках нет, то показано тускло и дословно,
// а не выдумано. Тексты владельца взяты из наряда дословно.
function renderHistory(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/history")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const sub = el("div", "row");
      sub.appendChild(el("div", "desc",
        "Что делали ноги, по дням. Строка — сообщение коммита, которым нога закончилась."));
      content.appendChild(sub);

      if (!data.count) {
        content.appendChild(el("div", "empty", "Пока ни одной ноги."));
      }
      for (const day of data.days || []) {
        const head = el("div", "group", day.date);
        content.appendChild(head);
        for (const r of day.rows) {
          const row = el("div", "row");
          if (r.text) {
            row.appendChild(el("div", "human", r.text));
          } else {
            row.appendChild(el("div", "human dim", "коммит не найден"));
          }
          const meta = el("div", "id");
          if (r.play) {
            meta.appendChild(document.createTextNode(r.play));
          } else {
            meta.appendChild(el("span", "dim", "плей не записан"));
          }
          meta.appendChild(document.createTextNode(" · " + r.leg));
          if (r.sha) meta.appendChild(document.createTextNode(" · " + r.sha));
          meta.appendChild(document.createTextNode(" · " + r.path));
          row.appendChild(meta);
          content.appendChild(row);
        }
      }

      if (data.archive) {
        const a = el("div", "row");
        a.appendChild(el("div", "desc", "Прежний общий журнал направления лежит архивом:"));
        a.appendChild(el("div", "id", data.archive));
        content.appendChild(a);
      }

      content.appendChild(el("div", "numbers",
        "Всего ног: " + data.count + ". Без сообщения: " + data.without_commit
        + ". Без плея: " + data.without_play + "."));
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

// Раздел «ЗНАНИЯ»: принятые факты направления. Кто их читает — из самой
// записи; устаревание никто не вычисляет. Чего в записи нет, то показано
// тускло и дословно, а не выдумано. Тексты владельца взяты из наряда дословно.
function knowledgeMeta(row) {
  const meta = el("div", "id");
  const put = (node) => {
    if (meta.childNodes.length) meta.appendChild(document.createTextNode(" · "));
    meta.appendChild(node);
  };
  // Дата принятия уже стоит в голове строки — второй раз её здесь не печатаем.
  put(row.status
    ? document.createTextNode(row.status)
    : el("span", "dim", "статус не проставлен"));
  if (row.source) put(document.createTextNode(row.source));
  return meta;
}

function knowledgeRowView(r) {
  const row = el("div", "row");
  // Дата принятия уходит вправо в голову строки — туда же, где даты во всех
  // остальных разделах. Искать её глазами в потоке служебной подписи не надо.
  const head = el("div", "rowhead");
  head.appendChild(el("span", "status quiet", "ЗНАНИЕ"));
  if (r.accepted) head.appendChild(el("span", "when", String(r.accepted).slice(0, 10)));
  row.appendChild(head);
  row.appendChild(el("div", "title", r.title));
  row.appendChild(knowledgeMeta(r));
  // Кто читает — самое полезное в записи, поэтому отдельной строкой.
  if (r.reader) {
    row.appendChild(el("div", "human", r.reader));
  } else {
    row.appendChild(el("div", "human dim", "читатель не назван"));
  }
  if (r.body) {
    const details = el("div", "details");
    details.hidden = true;
    // Тело записи — человеческий текст целым документом, а не служебная
    // подпись: класс `human` несёт и меру строки, и вид заголовков с цитатами.
    details.appendChild(mdNode("div", "human", r.body));
    const toggleButton = el("button", "act", "подробности");
    toggleButton.addEventListener("click", () => {
      details.hidden = !details.hidden;
    });
    row.appendChild(toggleButton);
    row.appendChild(details);
  }
  row.appendChild(el("div", "id", r.path));
  return row;
}

function renderKnowledge(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/knowledge")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      const sub = el("div", "row");
      sub.appendChild(el("div", "desc",
        "Принятые факты. Кто их читает — из самой записи; устаревание никто не вычисляет."));
      content.appendChild(sub);

      if (!data.count) {
        content.appendChild(el("div", "empty", "Пока ни одной записи."));
      }
      for (const r of data.rows || []) content.appendChild(knowledgeRowView(r));

      content.appendChild(el("div", "numbers",
        "Всего записей: " + data.count + ". Без читателя: " + data.without_reader
        + ". Без статуса: " + data.without_status + "."));
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

// Раздел «НАПРАВЛЕНИЕ»: устав направления. Панель его не оценивает и не считает
// выполненным. Тексты владельца взяты из наряда дословно.
function renderDirection2(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/direction")
    .then((response) => { if (!response.ok) throw new Error("HTTP " + response.status); return response.json(); })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";

      // Полоса сроков — самая первая в разделе, до прогноза и до хартии.
      const bar = deadlinesBar(data.deadlines);
      if (bar) content.appendChild(bar);

      const sub = el("div", "row");
      sub.appendChild(el("div", "desc",
        "Устав направления. Панель его не оценивает и не считает выполненным."));
      content.appendChild(sub);

      // Прогноз идёт первым. Нет карточки — отсутствие показывается как отсутствие.
      const fr = el("div", "row");
      const f = data.forecast;
      if (f) {
        fr.appendChild(el("div", "status",
          "ПРОГНОЗ" + (f.status ? " · " + f.status : "")
          + (f.as_of ? " · на " + f.as_of : "")));
        if (f.target) fr.appendChild(el("div", "title", f.target));
        if (f.basis) fr.appendChild(mdNode("div", "human", f.basis));
        if (Array.isArray(f.drivers) && f.drivers.length) {
          const md = f.drivers.map((d) => "- " + d).join("\n\n");
          fr.appendChild(mdNode("div", "human", md));
        }
      } else {
        fr.appendChild(el("div", "human dim", "Прогноза у направления нет."));
      }
      content.appendChild(fr);

      // Хартия: раздел на блок, первый раскрыт, остальные — по кнопке,
      // как в «Знаниях». Имена разделов приходят из файла, не из кода.
      const secs = (data.charter && data.charter.sections) || [];
      if (!secs.length) {
        content.appendChild(el("div", "empty", "Хартии у направления нет."));
      }
      secs.forEach((s, i) => {
        const row = el("div", "row");
        row.appendChild(el("div", "title", s.title));
        if (i === 0) {
          row.appendChild(mdNode("div", "human", s.body));
        } else {
          const details = el("div", "details");
          details.hidden = true;
          details.appendChild(mdNode("div", "human", s.body));
          const toggleButton = el("button", "act", "подробности");
          toggleButton.addEventListener("click", () => {
            details.hidden = !details.hidden;
          });
          row.appendChild(toggleButton);
          row.appendChild(details);
        }
        content.appendChild(row);
      });

      // Внизу — реестр подписей одной строкой (целиком он стена) и дата
      // последнего изменения хартии. Чего нет, то показано как недостающее.
      const foot = el("div", "row");
      if (data.approvals) {
        foot.appendChild(el("div", "desc",
          "Реестр подписей: " + data.approvals.words
          + " слов одной записью, читается плохо."));
        foot.appendChild(el("div", "id", data.approvals.path));
      }
      const changed = data.charter && data.charter.changed;
      foot.appendChild(el("div", "desc",
        changed ? "Хартия менялась: " + changed + "." : "Хартия менялась: неизвестно."));
      content.appendChild(foot);
    })
    .catch((e) => { content.textContent = ""; content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e)); });
}

function renderSlots(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/slots")
    .then((response) => {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    })
    .then((data) => {
    if (token !== RENDER_TOKEN) return;
    content.textContent = "";
    if (data.error) {
      content.appendChild(el("div", "empty", "ДОСКИ СЛОТОВ НЕТ"));
      const how = el("div", "row");
      how.appendChild(el("div", "desc", data.error));
      content.appendChild(how);
      return;
    }
    const free = data.slots.filter((s) => s.lifecycle === "AVAILABLE").length;
    const nums = el("div", "numbers");
    nums.appendChild(el("span", "num", "свободно " + free + " из " + data.slots.length));
    nums.appendChild(el("span", "num", "доска вне репозитория"));
    content.appendChild(nums);

    for (const s of data.slots) {
      const row = el("div", "row");
      const busy = s.lifecycle === "CLAIMED";
      row.appendChild(el("div", busy ? "status wait" : "status",
        (busy ? "ЗАНЯТ" : "СВОБОДЕН") + " · слот " + s.slot));
      row.appendChild(el("div", busy ? "title" : "title dim",
        busy ? s.call : "готов принять работу"));
      if (busy && s.stage) row.appendChild(el("div", "desc", "стадия: " + s.stage));

      if (!s.branch_exists) {
        row.appendChild(el("div", "desc", "рабочей копии ещё нет"));
      } else {
        if (s.worktree) row.appendChild(el("div", "desc", s.worktree));
        if (s.clean === false) row.appendChild(el("div", "waitline", "копия грязная"));
        if (s.ahead) {
          row.appendChild(el("div", "waitline",
            "не опубликовано: " + s.ahead + " — освободить слот сейчас значит похоронить их"));
        }
      }
      row.appendChild(el("div", "id", s.branch));
      content.appendChild(row);
    }

    const where = el("div", "row");
    where.appendChild(el("div", "id", data.ledger));
    content.appendChild(where);
  }).catch((e) => {
    content.textContent = "";
    content.appendChild(el("div", "empty", "НЕ ОТВЕЧАЕТ: " + e));
  });
}

function renderDirection(direction, sectionId) {
  const nav = document.getElementById("nav");
  const content = document.getElementById("content");
  nav.textContent = "";
  content.textContent = "";

  for (const section of direction.sections) {
    const link = el("a", section.ready ? "" : "off", section.label);
    if (section.id === sectionId) link.classList.add("active");
    if (section.ready) {
      link.href = "#/" + direction.id + "/" + section.id;
    } else {
      link.addEventListener("click", (event) => event.preventDefault());
    }
    nav.appendChild(link);
  }

  const section = direction.sections.find((s) => s.id === sectionId) || null;
  if (!section) {
    content.appendChild(el("div", "empty", "РАЗДЕЛ ПУСТ"));
    return;
  }
  if (!section.ready) {
    content.appendChild(el("div", "empty", "РАЗДЕЛ ЕЩЁ НЕ СДЕЛАН"));
    return;
  }
  if (sectionId === "dashboard") {
    renderDashboard(direction, content);
    return;
  }
  if (sectionId === "slots") {
    renderSlots(direction, content);
    return;
  }
  if (sectionId === "waiting") {
    renderWaiting(direction, content);
    return;
  }
  if (sectionId === "wave") {
    renderWave(direction, content);
    return;
  }
  if (sectionId === "ideas") {
    renderIdeas(direction, content);
    return;
  }
  if (sectionId === "history") {
    renderHistory(direction, content);
    return;
  }
  if (sectionId === "knowledge") {
    renderKnowledge(direction, content);
    return;
  }
  if (sectionId === "direction") {
    renderDirection2(direction, content);
    return;
  }
  if (sectionId === "goals") {
    if (ROUTE_EXTRA) renderGoalPage(direction, ROUTE_EXTRA, content);
    else renderGoals(direction, content);
    return;
  }
  content.appendChild(el("div", "empty", "РАЗДЕЛ ПУСТ"));
}

function render() {
  RENDER_TOKEN += 1;
  const route = parseHash();
  renderTopbar(route);
  if (!route.direction) {
    renderPicker();
    return;
  }
  const direction = findDirection(route.direction);
  if (!direction) {
    renderPicker();
    return;
  }
  // Умолчание — ПЕРВЫЙ готовый раздел, а не имя в коде: закроешь раздел, и
  // ссылка по умолчанию сама перестанет на него вести.
  const first = (direction.sections || []).find((s) => s.ready);
  renderDirection(direction, route.section || (first && first.id) || "wave");
}

function start() {
  fetch("/api/state")
    .then((response) => response.json())
    .then((state) => {
      STATE = state;
      window.addEventListener("hashchange", render);
      render();
    })
    .catch(() => {
      const content = document.getElementById("content");
      content.textContent = "";
      content.appendChild(el("div", "problem", "НЕ УДАЛОСЬ ЗАГРУЗИТЬ СОСТОЯНИЕ"));
    });
}

start();
