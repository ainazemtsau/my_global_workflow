// Маленький отрисовщик markdown для панели. Экспортирует window.mdToHtml(text).
// Поддерживает ровно: **жирный**, `код`, списки "- ", абзацы через пустую строку,
// перевод строки внутри абзаца -> <br>. Всё прочее — как текст.
// Любой <, > и & экранируется ДО разметки: описания содержат угловые скобки.
// Ссылки, картинки и заголовки не поддерживаются и в выводе появиться не могут.
(function () {
  "use strict";

  function escapeHtml(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // Вход уже экранирован, поэтому разметка добавляется только своими маркерами.
  function inline(text) {
    return text
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  function mdToHtml(text) {
    if (text == null) return "";
    const lines = String(text).split("\n").map(escapeHtml);
    const out = [];
    let para = [];
    let list = [];

    function flushPara() {
      if (para.length > 0) {
        out.push("<p>" + para.join("<br>") + "</p>");
        para = [];
      }
    }

    function flushList() {
      if (list.length > 0) {
        out.push("<ul><li>" + list.join("</li><li>") + "</li></ul>");
        list = [];
      }
    }

    for (const line of lines) {
      if (line.startsWith("- ")) {
        flushPara();
        list.push(inline(line.slice(2)));
      } else if (line === "") {
        flushPara();
        flushList();
      } else {
        flushList();
        para.push(inline(line));
      }
    }
    flushPara();
    flushList();
    return out.join("\n");
  }

  window.mdToHtml = mdToHtml;
})();
