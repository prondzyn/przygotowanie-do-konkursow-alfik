"""Wstawia zadania z oryginalnych arkuszy (testy-przeszle/alfik-RRRR.md) do działów
w zadania-wg-typu/ według narzedzia/klasyfikacja.json.

Każde wstawione zadanie dostaje znacznik *(Alfik RRRR, zad. N)*. Skrypt można uruchamiać
wielokrotnie: najpierw usuwa z działów wszystkie zadania z takim znacznikiem, potem wstawia
je na nowo, numeruje zadania od 1 i odtwarza klucz odpowiedzi.

Użycie:  python narzedzia/scal_oryginaly.py   (potem python zbuduj.py)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DZIALY = ROOT / "zadania-wg-typu"
PRZESZLE = ROOT / "testy-przeszle"
KLASYFIKACJA = Path(__file__).resolve().parent / "klasyfikacja.json"

TAG = re.compile(r" \*\(Alfik (\d{4}), zad\. (\d+)\)\*")
PKT = re.compile(r"\*\(([345]) pkt\)\*")


def split_tasks(lines):
    """Dzieli linie na tekst przed zadaniami i bloki zadań (bez numeru na początku)."""
    intro, tasks, cur = [], [], None
    for line in lines:
        m = re.match(r"^\d+\. (.*)$", line)
        if m:
            cur = [m.group(1)]
            tasks.append(cur)
        elif cur is not None and (line.startswith(" ") or line == "" and not cur[-1].endswith("</details><br>")):
            cur.append(line)
        elif cur is not None and line == "":
            continue
        else:
            if tasks:
                raise ValueError(f"Nieoczekiwana linia po zadaniach: {line[:60]!r}")
            intro.append(line)
    return intro, tasks


def answer(task):
    det = next(l for l in task if "<details>" in l)
    return re.search(r"</summary>([A-E] — .*?)<br>", det).group(1)


def points(task):
    return int(PKT.search(task[0]).group(1))


def past_tasks():
    out = {}
    for f in PRZESZLE.glob("alfik-*.md"):
        year = re.search(r"\d{4}", f.stem).group(0)
        body = f.read_text(encoding="utf-8").split("## Klucz odpowiedzi")[0]
        lines = [l for l in body.split("\n") if not l.startswith("## ") and l.strip() != "---"]
        start = next(i for i, l in enumerate(lines) if re.match(r"^1\. ", l))
        _, tasks = split_tasks(lines[start:])
        for nr, t in enumerate(tasks, 1):
            t = [l for l in t if l != ""]
            t[0] = t[0] + f" *(Alfik {year}, zad. {nr})*"
            out[(year, nr)] = t
    return out


def merge(path, inserts):
    text = path.read_text(encoding="utf-8")
    head, rest = text.split("\n## ", 1)
    body, tail = rest.split("\n---\n\n## Klucz odpowiedzi", 1)
    after_key = tail[tail.index("\n## "):] if "\n## " in tail else ""

    sections = ("## " + body).split("\n## ")
    new_sections, numbered = [], []
    for sec in sections:
        sec = sec if sec.startswith("## ") else "## " + sec
        lines = sec.rstrip("\n").split("\n")
        heading = lines[0][3:].strip()
        intro, tasks = split_tasks(lines[1:])
        tasks = [t for t in tasks if not TAG.search(t[0])]
        extra = inserts.pop(heading, [])
        # Kolejność: od 3 do 5 pkt; przy tych samych punktach najpierw nasze, potem oryginalne (od najnowszych).
        keyed = [(points(t), 0, 0, i, t) for i, t in enumerate(tasks)]
        keyed += [(points(t), 1, -int(y), int(n), t) for (y, n), t in extra]
        keyed.sort(key=lambda k: k[:4])
        while intro and intro[-1] == "":
            intro.pop()
        new_sections.append((lines[0], intro, [k[4] for k in keyed]))

    if inserts:
        raise ValueError(f"{path.name}: brak podrozdziałów {list(inserts)}")

    out = [head.rstrip("\n"), ""]
    n = 0
    for heading, intro, tasks in new_sections:
        out += [heading] + intro + [""]
        for t in tasks:
            n += 1
            out.append(f"{n}. {t[0]}")
            out += [l for l in t[1:] if l != ""]
            numbered.append(t)
        out.append("")
    out += ["---", "", "## Klucz odpowiedzi", ""]
    for i, t in enumerate(numbered, 1):
        src = TAG.search(t[0])
        out.append(f"{i}. {answer(t)}" + (f" *(Alfik {src.group(1)}, zad. {src.group(2)})*" if src else ""))
    text = "\n".join(out) + "\n" + after_key

    # Linia „W pliku: …” w nagłówku
    orig = sum(1 for t in numbered if TAG.search(t[0]))
    cnt = {p: sum(1 for t in numbered if points(t) == p) for p in (3, 4, 5)}
    summary = (f"- **W pliku:** {len(numbered)} zadań: {len(numbered) - orig} nowych i {orig} z prawdziwych "
               f"arkuszy Alfika ({cnt[3]} za 3 pkt, {cnt[4]} za 4 pkt, {cnt[5]} za 5 pkt).")
    text = re.sub(r"^- \*\*W pliku:\*\*.*$", summary, text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return len(numbered), orig


def main():
    klas = json.loads(KLASYFIKACJA.read_text(encoding="utf-8"))
    tasks = past_tasks()
    plan = {}
    for year, items in klas.items():
        for it in items:
            key = (year, it["nr"])
            plan.setdefault(it["plik"], {}).setdefault(it["podrozdzial"], []).append((key, tasks[key]))
    for f in sorted(DZIALY.glob("[0-9][0-9]-*.md")):
        total, orig = merge(f, plan.pop(f.name, {}))
        print(f"{f.name}: {total} zadań, w tym {orig} z arkuszy")
    if plan:
        raise ValueError(f"Nieznane pliki w klasyfikacji: {list(plan)}")


if __name__ == "__main__":
    main()
