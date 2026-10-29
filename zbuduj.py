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

# (ścieżka, id strony, rodzaj, krótka nazwa)
STALE = [
    ("README.md", "start", "info", "Start"),
    ("zadania-wg-typu/README.md", "dzialy", "info", "Zadania wg typu"),
    ("testy-przeszle/README.md", "przeszle", "info", "Testy przeszłe"),
    ("testy-probne/README.md", "testy", "info", "Testy próbne"),
]


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


def pages():
    out = []
    for path, pid, kind, short in STALE:
        f = ROOT / path
        if f.exists():
            out.append({"path": path, "id": pid, "kind": kind, "short": short, "md": fix_indent(f.read_text(encoding="utf-8"))})
    for f in sorted((ROOT / "zadania-wg-typu").glob("[0-9][0-9]-*.md")):
        md = fix_indent(f.read_text(encoding="utf-8"))
        title = short_name(md, f.stem)
        # „01. Kalendarz i zegar” -> „01 Kalendarz i zegar”
        title = re.sub(r"^(\d+)\.\s*", r"\1 ", title)
        out.append({"path": f"zadania-wg-typu/{f.name}", "id": f.stem, "kind": "dzial", "short": title, "md": md})
    # Oryginalne arkusze od najnowszego
    for f in sorted((ROOT / "testy-przeszle").glob("alfik-*.md"), reverse=True):
        md = fix_indent(f.read_text(encoding="utf-8"))
        out.append({"path": f"testy-przeszle/{f.name}", "id": f.stem, "kind": "przeszly", "short": short_name(md, f.stem), "md": md})
    for f in sorted((ROOT / "testy-probne").glob("test-*.md"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
        md = fix_indent(f.read_text(encoding="utf-8"))
        out.append({"path": f"testy-probne/{f.name}", "id": f.stem, "kind": "test", "short": short_name(md, f.stem), "md": md})
    return out


def build():
    lista = pages()
    data = json.dumps(lista, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*PAGES*/", data)
    (ROOT / "index.html").write_text("<!doctype html>\n<html lang=\"pl\">\n" + html + "</html>\n", encoding="utf-8")
    print(f"index.html: {len(lista)} stron")


if __name__ == "__main__":
    build()
