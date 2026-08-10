// Отрисовщик markdown для панели. Экспортирует window.mdToHtml(text).
//
// Панель существует, чтобы владелец НЕ ЧИТАЛ markdown. Значит разметка,
// доехавшая до экрана, — отказ. Прежняя версия умела только **жирный**, `код`
// и списки «- »: её писали под однострочные описания карточек, а потом ей
// скормили целый документ знания, и на экран уехали решётки заголовков,
// «птички» цитат, палки таблиц и служебный END_OF_FILE.
//
// Поддерживается ровно то, что реально встречается в состоянии (замерено
// 2026-08-09 по всем записям знаний): заголовки `#`..`####`, цитаты `> `,
// таблицы, списки «- » и «1. », **жирный**, `код`, абзацы.
//
// ДВА ПРАВИЛА, НА КОТОРЫХ ВСЁ ДЕРЖИТСЯ:
//   1. Экранирование идёт ПЕРВЫМ, до всякой разметки. Вывод уходит в innerHTML,
//      поэтому чужой тег обязан стать текстом, а не тегом.
//   2. Одиночный перенос строки внутри абзаца — ПРОБЕЛ, а не <br>. Файлы
//      состояния свёрстаны по ширине, и <br> на каждой строке рвал предложения
//      посреди мысли. Абзацы делит пустая строка, как и положено в markdown.
//
// Приёмка: node panel/test_md.cjs
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

  function cells(line) {
    // "| a | b |" -> ["a", "b"]. Крайние палки — оформление, а не ячейки.
    return line.replace(/^\||\|$/g, "").split("|").map(function (c) {
      return inline(c.trim());
    });
  }

  function isDivider(line) {
    return /^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?$/.test(line.trim());
  }

  function mdToHtml(text) {
    if (text == null) return "";
    const lines = String(text).split("\n").map(escapeHtml);
    const out = [];
    let para = [];
    let quote = [];
    let items = [];
    let ordered = false;
    let table = [];

    function flushPara() {
      if (para.length) {
        out.push("<p>" + inline(para.join(" ")) + "</p>");
        para = [];
      }
    }
    function flushQuote() {
      if (quote.length) {
        out.push("<blockquote><p>" + inline(quote.join(" ")) + "</p></blockquote>");
        quote = [];
      }
    }
    function flushList() {
      if (items.length) {
        const tag = ordered ? "ol" : "ul";
        out.push("<" + tag + "><li>" + items.join("</li><li>") + "</li></" + tag + ">");
        items = [];
      }
    }
    function flushTable() {
      if (!table.length) return;
      const rows = table.filter(function (r) { return !isDivider(r); });
      const head = cells(rows[0] || "");
      const body = rows.slice(1);
      let html = "<table><thead><tr><th>" + head.join("</th><th>") + "</th></tr></thead>";
      if (body.length) {
        html += "<tbody>";
        for (const r of body) {
          html += "<tr><td>" + cells(r).join("</td><td>") + "</td></tr>";
        }
        html += "</tbody>";
      }
      out.push(html + "</table>");
      table = [];
    }
    function flushAll() {
      flushPara();
      flushQuote();
      flushList();
      flushTable();
    }

    for (const line of lines) {
      const heading = /^(#{1,4})\s+(.*)$/.exec(line);
      const bullet = /^\s*[-*]\s+(.*)$/.exec(line);
      const number = /^\s*\d+\.\s+(.*)$/.exec(line);

      // Хвост файла — служебная строка носителя. На экране ей делать нечего.
      if (line.startsWith("END_OF_FILE:")) {
        flushAll();
      } else if (line.trim() === "") {
        flushAll();
      } else if (heading) {
        flushAll();
        // `#` в теле — это подзаголовок внутри страницы, а не заголовок страницы:
        // её название панель уже показала своей строкой. Поэтому со второго уровня.
        const level = Math.min(heading[1].length + 1, 4);
        out.push("<h" + level + ">" + inline(heading[2].trim()) + "</h" + level + ">");
      } else if (line.startsWith("&gt; ") || line === "&gt;") {
        flushPara();
        flushList();
        flushTable();
        quote.push(line.slice(5).trim());
      } else if (line.trim().startsWith("|")) {
        flushPara();
        flushQuote();
        flushList();
        table.push(line.trim());
      } else if (bullet || number) {
        flushPara();
        flushQuote();
        flushTable();
        const wanted = Boolean(number);
        if (items.length && wanted !== ordered) flushList();
        ordered = wanted;
        items.push(inline((bullet ? bullet[1] : number[1]).trim()));
      } else {
        flushQuote();
        flushList();
        flushTable();
        para.push(line.trim());
      }
    }
    flushAll();
    return out.join("\n");
  }

  window.mdToHtml = mdToHtml;
})();
