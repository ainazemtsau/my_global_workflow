import { existsSync } from "node:fs";
import { isAbsolute, relative, resolve, sep } from "node:path";

// Куда Pi МОЖЕТ писать. Всё остальное в репозитории — только чтение.
// Действующий workflow (os/, live/) меняется исключительно применением RESULT,
// поэтому Pi к нему не допускается вообще, а не "с осторожностью".
const WRITE_ALLOWED = ["tools", "os2", ".pi"];

// Замороженные материалы: читать без явного слова владельца нельзя.
const READ_DENIED = ["archive"];

const BANNED_BASH: Array<[RegExp, string]> = [
  [
    /\bgit\s+(commit|push|add|reset|checkout|restore|clean|rebase|merge|switch|worktree|stash|tag)\b/,
    "git-операции выполняет писатель, не Pi",
  ],
  [/\brm\s+-[A-Za-z]*r/, "рекурсивное удаление"],
  [/\bsed\s+-i\b/, "правка файла на месте через sed"],
  [
    /[>]{1,2}\s*['"]?(\.\/)?((live|os|archive)\/|AGENTS\.md|CLAUDE\.md)/,
    "перенаправление вывода в защищённый путь",
  ],
  [
    /\b(mv|cp|rm|truncate|tee|install)\b[^|;&]*\b(live|os|archive)\//,
    "изменение защищённой папки",
  ],
  [/\bnpm\s+(publish|link)\b|\bnpm\s+i(nstall)?\s+-g\b/, "глобальная установка или публикация"],
];

function findRepoRoot(start: string): string | null {
  let dir = resolve(start);
  for (let i = 0; i < 40; i++) {
    if (existsSync(resolve(dir, ".git"))) return dir;
    const up = resolve(dir, "..");
    if (up === dir) return null;
    dir = up;
  }
  return null;
}

const ROOT = findRepoRoot(process.cwd());

// Первый сегмент пути относительно корня репозитория.
// null означает "не смог разобрать или вне репозитория" — такой путь трактуется как запрещённый.
function segmentOf(p: unknown): string | null {
  if (typeof p !== "string" || p.length === 0) return null;
  if (!ROOT) return null;
  const abs = isAbsolute(p) ? resolve(p) : resolve(process.cwd(), p);
  const r = relative(ROOT, abs);
  if (r === "" || r.startsWith("..")) return null;
  return r.split(sep).join("/").split("/")[0];
}

export default function guard(pi: any) {
  // Не нашли корень репозитория — сторож не знает границ и блокирует всё.
  // Отказ громкий: молчаливый пропуск здесь опаснее остановки.
  if (!ROOT) {
    pi.on("tool_call", async () => ({
      block: true,
      reason:
        "guard.ts: не найден корень репозитория, границы неизвестны — заблокировано всё. Запусти pi из папки внутри репозитория.",
    }));
    return;
  }

  pi.on("tool_call", async (event: any) => {
    const tool = event?.toolName;

    if (tool === "write" || tool === "edit") {
      const seg = segmentOf(event?.input?.path);
      if (seg === null) {
        return {
          block: true,
          reason: `guard.ts: путь вне репозитория или не разобран — запись запрещена. path=${String(
            event?.input?.path,
          )}`,
        };
      }
      if (!WRITE_ALLOWED.includes(seg)) {
        return {
          block: true,
          reason: `guard.ts: писать можно только в ${WRITE_ALLOWED.map((d) => d + "/").join(", ")}. Путь начинается с "${seg}/" — это действующий workflow, он меняется только применением RESULT. Если задача правда требует его тронуть — остановись и скажи владельцу, не обходи.`,
        };
      }
    }

    if (tool === "read") {
      const seg = segmentOf(event?.input?.path);
      if (seg !== null && READ_DENIED.includes(seg)) {
        return {
          block: true,
          reason:
            "guard.ts: archive/ — замороженные материалы. Читать их можно только с явного разрешения владельца.",
        };
      }
    }

    if (tool === "bash") {
      const cmd = String(event?.input?.command ?? "");
      for (const [re, why] of BANNED_BASH) {
        if (re.test(cmd)) {
          return {
            block: true,
            reason: `guard.ts: ${why}. Команда заблокирована: ${cmd.slice(0, 200)}`,
          };
        }
      }
    }
  });
}
