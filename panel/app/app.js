// Панель направлений. Роутинг на хэшах, без перезагрузки страницы.
// Весь вид — только классами из style.css: своих классов и инлайн-стилей нет.
// innerHTML получает ТОЛЬКО вывод window.mdToHtml — тот экранирует входной текст.

let STATE = null;
// Токен отрисовки: ответ fetch, пришедший после ухода со страницы, не рисуется.
let RENDER_TOKEN = 0;

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

function parseHash() {
  const parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
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
    link.href = "#/" + d.id + "/now";
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
}

function renderPicker() {
  const nav = document.getElementById("nav");
  nav.textContent = "";
  const content = document.getElementById("content");
  content.textContent = "";
  for (const d of STATE.directions) {
    const row = el("a", "row");
    row.href = "#/" + d.id + "/now";
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

// Раздел «Сейчас»: строка чисел, готовые к запуску наряды, ниже — всё остальное.
function renderNow(direction, content) {
  const token = ++RENDER_TOKEN;
  fetch("/api/section/" + encodeURIComponent(direction.id) + "/now")
    .then((response) => {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    })
    .then((data) => {
      if (token !== RENDER_TOKEN) return;
      content.textContent = "";
      renderNumbers(content, data.numbers);
      if (data.ready.length > 0) {
        for (const order of data.ready) renderOrderRow(content, order, true);
      } else {
        content.appendChild(el("div", "empty", "ЗАПУСКАТЬ НЕЧЕГО"));
      }
      for (const order of data.other) renderOrderRow(content, order, false);
      if (data.unread.length > 0) {
        const names = data.unread.map((u) => u.file).join(", ");
        content.appendChild(
          el("div", "problem", "НЕ ПРОЧИТАЛОСЬ " + data.unread.length + " — " + names)
        );
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
  const st = (r.status || "нет статуса").toUpperCase();
  const cls = r.status === "done" ? "status" : (r.status === "open" ? "status wait" : "status wait");
  row.appendChild(el("div", cls, st + (r.order ? " · " + r.order : "")));
  row.appendChild(el("div", r.status === "done" ? "title dim" : "title", r.goal || r.id));
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

function goalRow(n, tone) {
  const row = el("div", "goal " + tone);
  row.appendChild(el("div", "goal-name", n.label || n.id));
  const sub = el("div", "goal-hook");
  sub.textContent = (n.hook || "") + (n.hook ? " · " : "") + n.id;
  row.appendChild(sub);
  const d = el("details", "goal-more");
  d.appendChild(el("summary", "act", "подробнее"));
  const inner = el("div", "details");
  if (n.goal) { const x = el("div", "desc"); x.innerHTML = window.mdToHtml("**цель:** " + n.goal); inner.appendChild(x); }
  if (n.why) { const x = el("div", "desc"); x.innerHTML = window.mdToHtml("**зачем:** " + n.why); inner.appendChild(x); }
  if (n.done_when) { const x = el("div", "desc"); x.innerHTML = window.mdToHtml("**чем закрывается:** " + n.done_when); inner.appendChild(x); }
  if (n.detail) inner.appendChild(el("div", "id", n.detail));
  d.appendChild(inner);
  row.appendChild(d);
  return row;
}

function goalGroup(content, word, tone, rows, emptyText) {
  const head = el("div", "group " + tone);
  head.textContent = word + " — " + rows.length;
  content.appendChild(head);
  if (!rows.length) {
    content.appendChild(el("div", "group-empty", emptyText || "пусто"));
    return;
  }
  for (const n of rows) content.appendChild(goalRow(n, tone));
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
        t.textContent = "ближайшая дата: " + data.target;
        top.appendChild(t);
      }
      content.appendChild(top);

      const g = data.groups || {};
      goalGroup(content, "ИДЁТ СЕЙЧАС", "now", g.running || [], "ставка не выбрана");
      goalGroup(content, "ДАЛЬШЕ", "ahead", g.ahead || []);
      goalGroup(content, "СДЕЛАНО", "done", g.closed_done || []);

      const dropped = g.closed_dropped || [];
      if (dropped.length) {
        const d = el("details", "dropped");
        d.appendChild(el("summary", "group gone", "СНЯТО — " + dropped.length));
        for (const n of dropped) d.appendChild(goalRow(n, "gone"));
        content.appendChild(d);
      }

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
  if (sectionId === "now") {
    renderNow(direction, content);
    return;
  }
  if (sectionId === "slots") {
    renderSlots(direction, content);
    return;
  }
  if (sectionId === "wave") {
    renderWave(direction, content);
    return;
  }
  if (sectionId === "goals") {
    renderGoals(direction, content);
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
  renderDirection(direction, route.section || "now");
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
