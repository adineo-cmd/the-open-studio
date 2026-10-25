#!/usr/bin/env python3
"""One-shot port of the Astro repo to photography-dedicated content.

Run from the repo root. Transforms the kept src/raw pages (nav, footer,
tagline), git-rms the twelve non-photography pages (raw + astro), and
regenerates the client-side search index. The calling workflow deletes this
script and its own workflow file after running it.
"""

import pathlib
import re
import subprocess

ROOT = pathlib.Path(".")
KEEP = ["index", "genres", "profiles", "camera", "composition", "lighting",
        "editing", "gear", "terminology", "glossary", "history", "masters",
        "business", "learning", "search"]
REMOVE = ["crafts", "culinary", "digital", "filmmaking", "fitness",
          "gardening", "languages", "making", "music", "performing",
          "visual-arts", "writing"]

FOOTER = '''<h4>Library</h4>
        <ul>
          <li><a href="genres.html">Genres</a></li>
          <li><a href="profiles.html">Genre profiles</a></li>
          <li><a href="camera.html">Camera &amp; exposure</a></li>
          <li><a href="composition.html">Composition</a></li>
          <li><a href="lighting.html">Light &amp; lighting</a></li>
          <li><a href="editing.html">Editing &amp; workflow</a></li>
          <li><a href="gear.html">Gear &amp; optics</a></li>
          <li><a href="terminology.html">Terminology</a></li>
          <li><a href="glossary.html">Glossary</a></li>
          <li><a href="masters.html">Masters</a></li>
          <li><a href="history.html">History</a></li>
          <li><a href="business.html">Going pro</a></li>
          <li><a href="learning.html">Learning paths</a></li>
          <li><a href="search.html">Search</a></li>
        </ul>'''

report = []
for name in KEEP:
    p = ROOT / "src" / "raw" / f"{name}.html"
    if not p.exists():
        report.append(f"missing: {p}")
        continue
    t = p.read_text(encoding="utf-8")
    t2, n_nav = re.subn(r'<li class="has-sub">\s*<a href="crafts\.html".*?</ul>\s*</li>',
                        "", t, count=1, flags=re.S)
    t3, n_foot = re.subn(r"<h4>Library</h4>\s*<ul>.*?</ul>", FOOTER, t2, count=1, flags=re.S)
    t3 = t3.replace("<small>A free photography &amp; crafts library</small>",
                    "<small>A free photography library</small>")
    t3 = t3.replace(
        "A free, community-minded reference for photographers and makers of every level — genres, craft, light, editing, history, and the business of shooting, written to be read between sessions.",
        "A free, community-minded reference for photographers of every level — genres, craft, light, editing, history, and the business of shooting, written to be read between sessions.")
    t3 = t3.replace("Suggest a genre or craft", "Suggest a genre")
    if name == "index":
        t3 = t3.replace(
            "<title>The Open Studio — A free photography &amp; crafts reference library</title>",
            "<title>The Open Studio — A free photography reference library</title>")
        t3 = re.sub(r'<meta name="description" content="[^"]*">',
                    '<meta name="description" content="A free reference library for photography students: genres, exposure, composition, lighting, editing, history, masters, and the business of shooting. Open whenever you shoot.">',
                    t3, count=1)
        t3 = t3.replace(
            "The Open Studio is a free reference for people who make pictures — and people who make anything. Browse genres before you buy a camera, review exposure and lighting between shoots, study the masters, then wander eleven more studios — from music, cooking, and writing to film, gardening, fitness, and languages — no account, no fee, open whenever you are.",
            "The Open Studio is a free reference for students of photography. Browse genres before you pick a subject, review exposure and lighting between shoots, study the masters, and plan the business when you're ready — no account, no fee, open whenever you shoot.")
        t3 = t3.replace(
            "Twenty-six reading rooms, one building. Photography fills most of the shelf; eleven other fields have studios of their own, and every section cross-references the way working makers actually think.",
            "Fourteen reading rooms, one building. Each section stands on its own, and they cross-reference the way a working photographer actually thinks.")
        t3 = re.sub(r'\s*<a class="section-card" href="crafts\.html">.*?</a>\n', "\n", t3, count=1, flags=re.S)
    if t3 != t:
        p.write_text(t3, encoding="utf-8")
    report.append(f"{name}: nav_removed={n_nav} footer_replaced={n_foot}")

doomed = [str(ROOT / sub / f"{n}{ext}")
          for n in REMOVE for sub, ext in (("src/raw", ".html"), ("src/pages", ".astro"))]
existing = [f for f in doomed if pathlib.Path(f).exists()]
if existing:
    subprocess.run(["git", "rm", "-q", *existing], check=True)
report.append(f"removed {len(existing)} files")

subprocess.run(["python3", "tools/build_search_index.py"], check=True)
report.append("search index regenerated")

print("\n".join(report))
