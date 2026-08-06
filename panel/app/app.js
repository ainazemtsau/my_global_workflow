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
