# -*- coding: utf-8 -*-
"""Самопроверка osctl. Гоняется на ВРЕМЕННОЙ доске, живую не трогает.

Главный случай — C5: настоящая гонка двух процессов за один слот.
Без него «двое не захватят один слот» — это надежда, а не факт.

    python panel/test_osctl.py
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OSCTL = ROOT / "osctl.py"
D = "test-direction"

fails = []


def check(ok, msg):
    print(("OK   " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


def run(*args, env=None):
    e = dict(os.environ)
    e["PYTHONIOENCODING"] = "utf-8"
    if env:
        e.update(env)
    return subprocess.run([sys.executable, str(OSCTL), *args], cwd=str(ROOT),
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=e)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="osctl-test-"))
    os.environ["OSCTL_STATE_DIR"] = str(tmp)
    ledger = tmp / "slots" / f"{D}.json"

    r = run("slot", "list", "--direction", D)
    check(r.returncode == 1 and "доски слотов нет" in r.stderr,
          "без доски команда останавливается с человеческой причиной")

    r = run("slot", "init", "--direction", D, "--count", "4")
    check(r.returncode == 0 and ledger.exists(), "init создал доску")
    data = json.loads(ledger.read_text(encoding="utf-8"))
    check(data["schema"] == "osctl.slot-state.v1", "схема записана")
    check(len(data["slots"]) == 4 and all(v["lifecycle"] == "AVAILABLE"
                                          for v in data["slots"].values()),
          "четыре слота, все свободны")

    r = run("slot", "init", "--direction", D, "--count", "4")
    check(r.returncode == 1, "повторный init без --force отказывает")

    r = run("slot", "claim", "--direction", D, "--slot", "2", "--for", "c-a-001", "--stage", "BUILD")
    check(r.returncode == 0, "слот 2 захвачен")
    data = json.loads(ledger.read_text(encoding="utf-8"))
    check(data["slots"]["2"] == {"lifecycle": "CLAIMED", "lease": "c-a-001:BUILD"},
          "запись слота ровно та, что ожидается")
    check(all(data["slots"][s]["lifecycle"] == "AVAILABLE" for s in ("1", "3", "4")),
          "остальные слоты не тронуты")

    r = run("slot", "claim", "--direction", D, "--slot", "2", "--for", "c-b-002", "--stage", "PLAN")
    check(r.returncode == 1 and "занят" in r.stderr, "занятый слот повторно не берётся")

    # ТО, РАДИ ЧЕГО ВСЁ: тот же наряд из другого слота
    r = run("slot", "claim", "--direction", D, "--slot", "3", "--for", "c-a-001", "--stage", "PLAN")
    check(r.returncode == 1 and "уже взят слотом 2" in r.stderr,
          "тот же наряд из другого слота отбивается — двое над одной работой невозможны")

    r = run("slot", "release", "--direction", D, "--slot", "2", "--for", "c-a-001", "--stage", "PLAN")
    check(r.returncode == 1 and "не совпадает" in r.stderr,
          "освобождение с другой стадией отказывает: аренда сверяется побайтово")

    r = run("slot", "release", "--direction", D, "--slot", "2", "--for", "c-a-001", "--stage", "BUILD")
    check(r.returncode == 0, "слот 2 освобождён своей арендой")
    data = json.loads(ledger.read_text(encoding="utf-8"))
    check(data["slots"]["2"] == {"lifecycle": "AVAILABLE", "lease": "none"}, "слот 2 снова свободен")

    r = run("slot", "release", "--direction", D, "--slot", "2", "--for", "c-a-001", "--stage", "BUILD")
    check(r.returncode == 1 and "и так свободен" in r.stderr, "двойное освобождение отказывает")

    r = run("slot", "claim", "--direction", D, "--slot", "1", "--for", "c-x:y", "--stage", "BUILD")
    check(r.returncode == 1, "двоеточие внутри id наряда отвергается")

    # C5 — НАСТОЯЩАЯ ГОНКА: восемь процессов одновременно за один свободный слот
    procs = [subprocess.Popen([sys.executable, str(OSCTL), "slot", "claim", "--direction", D,
                               "--slot", "4", "--for", f"c-race-{i:03d}", "--stage", "BUILD"],
                              cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                              env={**os.environ, "PYTHONIOENCODING": "utf-8"})
             for i in range(8)]
    codes = [p.wait() for p in procs]
    winners = codes.count(0)
    check(winners == 1, f"гонка восьми процессов: победитель ровно один, получилось {winners}")
    data = json.loads(ledger.read_text(encoding="utf-8"))
    check(data["slots"]["4"]["lifecycle"] == "CLAIMED", "слот 4 занят после гонки")
    check(len(data["slots"]) == 4, "доска не испорчена гонкой")
    check(json.loads(ledger.read_text(encoding="utf-8")) == data, "файл читается стабильно")

    # замок не остался лежать
    check(not (tmp / "slots" / f"{D}.json.lock").exists(), "замок снят после всех операций")

    # испорченная доска — стоп, а не догадка
    ledger.write_text('{"schema":"чужая","slots":{}}', encoding="utf-8")
    r = run("slot", "list", "--direction", D)
    check(r.returncode == 1 and "устарела" in r.stderr,
          "чужая схема: стоп с подсказкой обновить копию, а не непонятная ошибка")

    print(f"\n{'ПРИНЯТО' if not fails else 'НЕ ПРИНЯТО: ' + str(len(fails)) + ' упало'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
