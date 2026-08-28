"use strict";

// Исполняет настоящий app.js над маленьким DOM-носителем. Никакой второй
// реализации вида здесь нет: проверка вызывает production renderDashboard,
// кликает его настоящие обработчики и сериализует наблюдаемое поведение.
const fs = require("fs");
const vm = require("vm");

const ROOT = require("path").resolve(__dirname, "..");
const BASE = process.argv[2];
const DIRECTIONS = process.argv.slice(3);

class FakeNode {
  constructor(tag, text) {
    this.tagName = tag;
    this.className = "";
    this.children = [];
    this.attributes = {};
    this.events = {};
    this.hidden = false;
    this.href = null;
    this._text = text == null ? "" : String(text);
    this.classList = {
      add: (...names) => {
        const parts = new Set(this.className.split(/\s+/).filter(Boolean));
        for (const name of names) parts.add(name);
        this.className = Array.from(parts).join(" ");
      },
    };
  }
  appendChild(child) { this.children.push(child); return child; }
  addEventListener(name, callback) { this.events[name] = callback; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  remove() {}
  get childNodes() { return this.children; }
  set textContent(value) { this._text = String(value); this.children = []; }
  get textContent() { return this._text + this.children.map((x) => x.textContent).join(""); }
  set innerHTML(value) { this._text = String(value).replace(/<[^>]*>/g, " "); this.children = []; }
}

function walk(node, predicate, out = []) {
  if (predicate(node)) out.push(node);
  for (const child of node.children) walk(child, predicate, out);
  return out;
}

function hasClass(node, name) {
  return node.className.split(/\s+/).includes(name);
}

function visibleText(node) {
  if (node.hidden) return "";
  return node._text + node.children.map(visibleText).join("");
}

const requests = [];
const document = {
  createElement: (tag) => new FakeNode(tag),
  createTextNode: (text) => new FakeNode("#text", text),
  getElementById: () => new FakeNode("div"),
  body: new FakeNode("body"),
};
const location = {hash: ""};
const sandbox = {
  document,
  location,
  navigator: {},
  console,
  Date,
  Number,
  String,
  Set,
  encodeURIComponent,
  setTimeout,
  clearTimeout,
  fetch: async (url, options = {}) => {
    requests.push({url: String(url), method: String(options.method || "GET").toUpperCase()});
    return globalThis.fetch(new URL(String(url), BASE), options);
  },
};
sandbox.window = {mdToHtml: (value) => String(value), addEventListener: () => {}};
vm.createContext(sandbox);
let source = fs.readFileSync(require("path").join(ROOT, "panel", "app", "app.js"), "utf8");
source = source.replace(/\nstart\(\);\s*$/, "\n;globalThis.__renderDashboard = renderDashboard;");
vm.runInContext(source, sandbox, {filename: "panel/app/app.js"});

async function renderOne(direction) {
  const content = new FakeNode("main");
  await sandbox.__renderDashboard({id: direction}, content);
  const blocks = walk(content, (n) => hasClass(n, "dash-block"));
  const before = visibleText(content);
  const hashBefore = location.hash;
  const blockFacts = blocks.map((block) => {
    const preview = walk(block, (n) => hasClass(n, "dash-preview"))[0];
    const more = walk(block, (n) => hasClass(n, "dash-more"))[0];
    const toggle = walk(block, (n) => hasClass(n, "dash-toggle"))[0];
    const previewRows = preview.children.filter((n) => hasClass(n, "dash-row"));
    const moreWasHidden = more.hidden;
    toggle.events.click();
    return {
      previewRows: previewRows.length,
      numberVisible: walk(block, (n) => hasClass(n, "dash-count")).length === 1,
      howVisible: walk(block, (n) => hasClass(n, "dash-how")).length === 1,
      moreWasHidden,
      moreOpened: more.hidden === false,
    };
  });
  const records = walk(content, (n) => hasClass(n, "dash-record"));
  const recordFacts = records.map((record) => {
    const button = walk(record, (n) => hasClass(n, "dash-row-main"))[0];
    const body = walk(record, (n) => hasClass(n, "dash-record-body"))[0];
    const wasHidden = body.hidden;
    button.events.click();
    return {wasHidden, opened: body.hidden === false, text: visibleText(body)};
  });
  const after = visibleText(content);
  const links = walk(content, (n) => n.tagName === "a").map((n) => ({href: n.href, text: n.textContent}));
  const charts = walk(content, (n) => hasClass(n, "dash-activity"));
  const inlineStyles = walk(content, (n) => Object.prototype.hasOwnProperty.call(n.attributes, "style"));
  const writeControls = walk(content, (n) => ["form", "input", "select", "textarea"].includes(n.tagName));
  return {
    direction,
    blockCount: blocks.length,
    blocks: blockFacts,
    recordFacts,
    chartCount: charts.length,
    chartCells: charts.reduce((sum, chart) => sum + chart.children.length, 0),
    links,
    before,
    after,
    hashUnchangedByToggles: location.hash === hashBefore,
    inlineStyleCount: inlineStyles.length,
    writeControlCount: writeControls.length,
  };
}

(async () => {
  const renders = [];
  for (const direction of DIRECTIONS) renders.push(await renderOne(direction));
  process.stdout.write(JSON.stringify({renders, requests}));
})().catch((error) => {
  process.stderr.write(String(error && error.stack || error));
  process.exitCode = 1;
});
