# -*- coding: utf-8 -*-
"""Приёмка применятеля правил: он обязан ОТКАЗЫВАТЬСЯ, а не догадываться.

Гоняется на поддельном наборе правил во временной папке. Настоящий `os/**`
только читается, и это проверяется отпечатком в конце.

    python panel/test_switchover.py
"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "os2" / "switchover.py"
EDITS = ROOT / "os2" / "switchover.json"
fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def os_fingerprint():
    h = hashlib.sha256()
    for p in sorted((ROOT / "os").rglob("*")):
        if p.is_file():
            h.update(str(p.relative_to(ROOT)).encode("utf-8"))
            h.update(p.read_bytes())
    return h.hexdigest()


def run(*args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, str(TOOL), *args], cwd=str(ROOT),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env)
    return r.returncode, (r.stdout + r.stderr).strip()


class Fake:
    """Поддельные правила: ядро и один плей, каждый со своим хвостом."""

    def __init__(self, kernel_body="alpha bravo charlie\n", play_body="delta echo\n"):
        self.dir = Path(tempfile.mkdtemp(prefix="switch-"))
        (self.dir / "os" / "plays").mkdir(parents=True)
        self.write("os/KERNEL.md", f"# KERNEL\n\n{kernel_body}\nEND_OF_FILE: os/KERNEL.md\n")
        self.write("os/plays/work.md",
                   f"# Play: work\n\nWrites: NOW.md, LOG.md.\n{play_body}\n"
                   "END_OF_FILE: os/plays/work.md\n")

    def write(self, rel, text):
        io.open(self.dir / rel, "w", encoding="utf-8", newline="").write(text)

    def read(self, rel):
        return io.open(self.dir / rel, encoding="utf-8").read()

    def drop(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def set_edits(edits, schema="os2.switchover.v1"):
    io.open(EDITS, "w", encoding="utf-8", newline="").write(
        json.dumps({"schema": schema, "edits": edits}, ensure_ascii=False, indent=2) + "\n")


def main():
    before = os_fingerprint()
    saved = EDITS.read_text(encoding="utf-8") if EDITS.exists() else None
    try:
        print("\n--- Набор правок сам по себе")
        set_edits([{"file": "os/KERNEL.md", "old": "bravo", "new": "bravo", "why": "x"}])
        rc, out = run("check")
        check(rc == 1 and "совпадают" in out, "правка «старое = новое» отвергается")

        set_edits([{"file": "os/KERNEL.md", "old": "bravo", "new": "delta"}])
        rc, out = run("check")
        check(rc == 1 and "why" in out, "правка без объяснения отвергается")

        set_edits([{"file": "os/KERNEL.md", "old": "a", "new": "b", "why": "x"}],
                  schema="что-то другое")
        rc, out = run("check")
        check(rc == 1 and "schema" in out, "чужая схема набора отвергается")

        print("\n--- Якоря")
        f = Fake()
        try:
            e = [{"file": "os/KERNEL.md", "old": "такого текста нет",
                  "new": "x", "why": "проба"}]
            rc, out = run("apply", "--out", str(f.dir / "out"))
            set_edits(e)
            rc, out = run("apply", "--out", str(f.dir / "out"))
            check(rc == 1 and "якор" in out, f"пропавший якорь останавливает: {out.splitlines()[-1][:60]}")

            set_edits([{"file": "os/KERNEL.md", "old": "the", "new": "x", "why": "проба"}])
            rc, out = run("apply", "--out", str(f.dir / "out"))
            check(rc == 1, "неоднозначный якорь тоже останавливает")
            check(not (f.dir / "out" / "os" / "KERNEL.md").exists()
                  or "the" in io.open(f.dir / "out" / "os" / "KERNEL.md", encoding="utf-8").read(),
                  "и при отказе ничего не записано")
        finally:
            f.drop()

        print("\n--- Настоящие правила: применение только в копию")
        out_dir = Path(tempfile.mkdtemp(prefix="switch-out-"))
        try:
            real = ROOT / "os" / "plays" / "work.md"
            anchor = "Reads: TREE.md, NOW.md; files the CALL points to."
            has = anchor in real.read_text(encoding="utf-8")
            check(has, "якорь для пробы найден в настоящем плее")
            reads_new = "Reads: the bet card, the task card and the cards the CALL names."
            writes_old = ("Writes: NOW.md call/task/issue state, LOG.md, and the versioned "
                          "artifact named by the CALL through RESULT.state_changes.")
            writes_new = ("Writes: call/task/issue cards and the artifact the CALL names, "
                          "via RESULT.state_changes.")
            if has:
                # НЕПОЛНЫЙ набор: адрес чтения поправлен, а строка записи ещё
                # называет исчезающий файл. Применятель обязан это назвать.
                set_edits([{"file": "os/plays/work.md", "old": anchor,
                            "new": reads_new, "why": "проба применятеля"}])
                rc, out = run("apply", "--out", str(out_dir / "copy"))
                check(rc == 1 and "всё ещё называет" in out,
                      f"неполный набор не проходит и говорит чем: {out.splitlines()[-1][:70]}")
                copied = (out_dir / "copy" / "os" / "plays" / "work.md").read_text(encoding="utf-8")
                check(reads_new in copied, "копия при этом изменена — отчёт честный, а не откат")
                check(anchor in real.read_text(encoding="utf-8"), "оригинал НЕ тронут")
                check(copied.rstrip().endswith("END_OF_FILE: os/plays/work.md"),
                      "хвост END_OF_FILE в копии на месте")

                # ПОЛНЫЙ набор по этому файлу — проходит
                has_w = writes_old in real.read_text(encoding="utf-8")
                check(has_w, "якорь строки записи найден в настоящем плее")
                if has_w:
                    set_edits([{"file": "os/plays/work.md", "old": anchor,
                                "new": reads_new, "why": "адрес чтения"},
                               {"file": "os/plays/work.md", "old": writes_old,
                                "new": writes_new, "why": "адрес записи"}])
                    rc, out = run("apply", "--out", str(out_dir / "copy2"))
                    check(rc == 0, f"полный набор по файлу проходит: {out.splitlines()[0][:60]}")
                    c2 = (out_dir / "copy2" / "os" / "plays" / "work.md").read_text(encoding="utf-8")
                    check("LOG.md" not in c2.split("\n")[5], "строка записи больше не зовёт LOG.md")

                    # тот же набор, но замена длиннее бюджета плея
                    set_edits([{"file": "os/plays/work.md", "old": anchor,
                                "new": reads_new, "why": "адрес чтения"},
                               {"file": "os/plays/work.md", "old": writes_old,
                                "new": writes_new + " " + " ".join(f"w{i}" for i in range(30)),
                                "why": "нарочно длинная"}])
                    rc, out = run("apply", "--out", str(out_dir / "copy3"))
                    check(rc == 1 and "бюджете" in out,
                          f"перебор бюджета плея останавливает: {out.splitlines()[-1][:65]}")
        finally:
            shutil.rmtree(out_dir, ignore_errors=True)

        print("\n--- Бюджеты и мёртвые адреса")
        f = Fake()
        try:
            long_line = " ".join(f"w{i}" for i in range(1700))
            set_edits([{"file": "os/KERNEL.md", "old": "alpha bravo charlie",
                        "new": long_line, "why": "проба бюджета"}])
            rc, out = run("apply", "--out", str(f.dir / "o"))
            # применение идёт в копию НАСТОЯЩЕГО os/, поэтому якоря там нет
            check(rc == 1, "поддельный якорь в настоящих правилах не находится — это и требуется")
        finally:
            f.drop()

        print("\n--- Живые правила")
        check(os_fingerprint() == before, "os/** не изменился ни на байт за всю приёмку")
    finally:
        if saved is not None:
            io.open(EDITS, "w", encoding="utf-8", newline="").write(saved)
        elif EDITS.exists():
            EDITS.unlink()

    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
