"""Składa wszystkie pliki .md w jeden plik index.html (działa po dwukliku, bez serwera).

Użycie:  python zbuduj.py
Po każdej zmianie w plikach .md uruchom ponownie.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "narzedzia" / "szablon.html"

# Strony informacyjne w katalogu klasy: (ścieżka, id strony, krótka nazwa)
STALE = [
    ("README.md", "start", "Start"),
    ("zadania-wg-typu/README.md", "dzialy", "Zadania wg typu"),
    ("testy-przeszle/README.md", "przeszle", "Testy przeszłe"),
    ("testy-probne/README.md", "testy", "Testy próbne"),
]
# Przed podziałem na konkursy strony matematyki dla klasy 5 miały id bez przedrostka.
# Strona przenosi pod nowe id zapisany postęp i stare linki.
DAWNA_KLASA = "matematyczny/klasa-5"


def short_name(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


def fix_indent(md: str) -> str:
    """Opcje i odpowiedź pisze się z wcięciem 3 spacji. Przy numerach dwucyfrowych (10. …)
    Markdown wymaga 4 spacji, inaczej opcje wypadają z zadania, więc wyrównujemy je tutaj."""
    out, width = [], 0
    for line in md.split("\n"):
        m = re.match(r"^(\d+)\. ", line)
        if m:
            width = len(m.group(1)) + 2
        elif width and re.match(r"^ {3}\S", line):
            line = " " * width + line[3:]
        elif line.strip() and not line.startswith(" "):
            width = 0
        out.append(line)
    return "\n".join(out)


def klasy():
    """Katalogi <konkurs>/klasa-<N>/ z plikiem README.md, np. matematyczny/klasa-5."""
    out = [d for d in ROOT.glob("*/klasa-*") if (d / "README.md").exists()]
    return sorted(out, key=lambda d: (d.parent.name, int(re.sub(r"\D", "", d.name) or 0)))


def pages_klasy(d: Path):
    rel = d.relative_to(ROOT).as_posix()
    nr = re.sub(r"\D", "", d.name)
    sek = {"id": f"{d.parent.name[:3]}{nr}", "nazwa": f"{d.parent.name.capitalize()} · kl. {nr}"}
    files = []
    for path, pid, short in STALE:
        if (d / path).exists():
            files.append((path, pid, "info", short))
    for f in sorted((d / "zadania-wg-typu").glob("[0-9][0-9]-*.md")):
        files.append((f"zadania-wg-typu/{f.name}", f.stem, "dzial", None))
    # Oryginalne arkusze od najnowszego
    for f in sorted((d / "testy-przeszle").glob("alfik-*.md"), reverse=True):
        files.append((f"testy-przeszle/{f.name}", f.stem, "przeszly", None))
    for f in sorted((d / "testy-probne").glob("test-*.md"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
        files.append((f"testy-probne/{f.name}", f.stem, "test", None))
    out = []
    for path, pid, kind, short in files:
        md = fix_indent((d / path).read_text(encoding="utf-8"))
        if short is None:
            short = short_name(md, pid)
            # „01. Kalendarz i zegar” -> „01 Kalendarz i zegar”
            short = re.sub(r"^(\d+)\.\s*", r"\1 ", short)
        page = {"path": f"{rel}/{path}", "id": f"{sek['id']}/{pid}", "kind": kind, "short": short,
                "sek": sek["id"], "sekNazwa": sek["nazwa"], "md": md}
        if rel == DAWNA_KLASA and pid != "start":
            page["dawne"] = pid
        out.append(page)
    return out


def pages():
    out = [{"path": "README.md", "id": "start", "kind": "info", "short": "Start", "md": (ROOT / "README.md").read_text(encoding="utf-8")}]
    for d in klasy():
        out += pages_klasy(d)
    return out


def build():
    lista = pages()
    data = json.dumps(lista, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*PAGES*/", data)
    (ROOT / "index.html").write_text("<!doctype html>\n<html lang=\"pl\">\n" + html + "</html>\n", encoding="utf-8")
    print(f"index.html: {len(lista)} stron")


if __name__ == "__main__":
    build()
