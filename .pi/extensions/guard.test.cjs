const PKG = "C:/Users/Anton/AppData/Roaming/npm/node_modules/@earendil-works/pi-coding-agent";
const createJiti = require(require.resolve("jiti", { paths: [PKG] }));
const jiti = createJiti(__filename, { interopDefault: true });

const mod = jiti("C:/my_global_workflow_worktrees/indie-game-development/.pi/extensions/guard.ts");
const guard = mod.default || mod;

let handler = null;
const fakePi = { on: (evt, fn) => { if (evt === "tool_call") handler = fn; } };
guard(fakePi);
if (!handler) { console.log("FAIL: guard did not register tool_call"); process.exit(1); }

const CASES = [
  ["write", { path: "os/KERNEL.md", content: "x" }, true, "запись в os/"],
  ["write", { path: "live/indie-game-development/NOW.md", content: "x" }, true, "запись в live/"],
  ["edit", { path: "AGENTS.md", edits: [] }, true, "правка AGENTS.md в корне"],
  ["write", { path: "C:/my_global_workflow_worktrees/indie-game-development/os/plays/day.md", content: "x" }, true, "абсолютный путь в os/"],
  ["write", { path: "tools/osctl/read_now.py", content: "x" }, false, "запись в tools/"],
  ["write", { path: "os2/cards/task.md", content: "x" }, false, "запись в os2/ (новая версия)"],
  ["write", { path: ".pi/extensions/foo.ts", content: "x" }, false, "запись в .pi/"],
  ["write", { path: "tools/../os/KERNEL.md", content: "x" }, true, "обход через .."],
  ["read", { path: "archive/anything.md" }, true, "чтение archive/"],
  ["read", { path: "os/KERNEL.md" }, false, "чтение os/ разрешено"],
  ["read", { path: "live/indie-game-development/NOW.md" }, false, "чтение live/ разрешено"],
  ["bash", { command: "git status --porcelain" }, false, "git status"],
  ["bash", { command: "git log --oneline -5" }, false, "git log"],
  ["bash", { command: "git commit -m x" }, true, "git commit"],
  ["bash", { command: "git push origin HEAD:main" }, true, "git push"],
  ["bash", { command: "rm -rf tools/osctl" }, true, "rm -rf"],
  ["bash", { command: "echo hi > live/x.md" }, true, "редирект в live/"],
  ["bash", { command: "echo hi > os2/x.md" }, false, "редирект в os2/ разрешён"],
  ["bash", { command: "sed -i s/a/b/ tools/x.py" }, true, "sed -i"],
  ["bash", { command: "python tools/osctl/verify.py" }, false, "прогон проверки"],
  ["bash", { command: "cp x.md live/indie/NOW.md" }, true, "cp в live/"],
];

let pass = 0, fail = 0;
(async () => {
  for (const [tool, input, shouldBlock, label] of CASES) {
    const r = await handler({ toolName: tool, input }, {});
    const blocked = !!(r && r.block);
    const ok = blocked === shouldBlock;
    if (ok) { pass++; } else { fail++; }
    console.log(`${ok ? "OK  " : "FAIL"}  ${shouldBlock ? "блок " : "пуск "} ${tool.padEnd(5)} ${label}`);
    if (!ok) console.log(`        got block=${blocked} reason=${r && r.reason}`);
  }
  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})();
