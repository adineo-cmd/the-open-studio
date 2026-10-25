#!/usr/bin/env python3
"""Build assets/js/search-data.js from the site's HTML pages.

Walks every page, collects headings, definition terms, and their surrounding
prose into SEARCH_DATA entries: {t: title, d: description, u: url, g: group}.

Run from the repository root:  python3 tools/build_search_index.py
Regenerate after any content edits.
"""

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "genres.html", "profiles.html", "camera.html",
    "composition.html", "lighting.html", "editing.html", "gear.html",
    "terminology.html", "glossary.html", "history.html", "masters.html",
    "business.html", "learning.html", "crafts.html", "music.html",
    "culinary.html", "writing.html", "making.html", "visual-arts.html",
    "performing.html", "digital.html", "filmmaking.html", "gardening.html",
    "fitness.html", "languages.html",
]

GROUP_NAMES = {
    "index.html": "Home",
    "genres.html": "Genres",
    "profiles.html": "Genre Profiles",
    "camera.html": "Camera & Exposure",
    "composition.html": "Composition",
    "lighting.html": "Light & Lighting",
    "editing.html": "Editing & Workflow",
    "gear.html": "Gear & Optics",
    "terminology.html": "Terminology",
    "glossary.html": "Glossary",
    "history.html": "History",
    "masters.html": "Masters",
    "business.html": "Going Pro",
    "learning.html": "Learning Paths",
    "crafts.html": "Every Field",
    "music.html": "Music",
    "culinary.html": "Cooking & Baking",
    "writing.html": "Writing",
    "making.html": "Woodworking & Making",
    "visual-arts.html": "Drawing & Painting",
    "performing.html": "Performing",
    "digital.html": "Programming & Design",
    "filmmaking.html": "Film & Video",
    "gardening.html": "Gardening & Growing",
    "fitness.html": "Strength & Movement",
    "languages.html": "Languages & Translation",
}

HEADING_TAGS = {"h1", "h2", "h3"}
BLOCK_TEXT_TAGS = {"p", "li", "dd", "figcaption", "td", "th"}
SKIP_TAGS = {"script", "style", "nav", "header", "footer"}


def clean(text):
    text = re.sub(r"\s+", " ", text).strip()
    return text


def truncate(text, limit=170):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + " …"


class PageParser(HTMLParser):
    def __init__(self, page, group):
        super().__init__(convert_charrefs=True)
        self.page = page
        self.group = group
        self.entries = []
        self.seen = set()

        self.in_main = False
        self.main_depth = 0
        self.skip_depth = 0
        self.id_stack = []          # open element ids
        self.current_id = page      # fallback anchor = page itself

        self.capture = None          # None | ("heading", ...) | ("dt", ...) | ("text", ...)
        self.capture_tag = None
        self.buffer = []
        self.capture_id = None
        self.heading_text = None
        self.awaiting_lead = False

    # -- helpers -------------------------------------------------------

    def add(self, title, desc, anchor):
        title, desc = clean(title), clean(desc)
        if not title:
            return
        key = (title, anchor)
        if key in self.seen:
            return
        self.seen.add(key)
        url = anchor if anchor != self.page else self.page
        self.entries.append({"t": title, "d": desc, "u": url, "g": self.group})

    def push(self, kind, tag, anchor):
        self.capture = kind
        self.capture_tag = tag
        self.buffer = []
        self.capture_id = anchor

    # -- parser hooks --------------------------------------------------

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
            self.main_depth = 1
            return
        if self.in_main and tag == "footer":
            # footer lives inside body after main; main already closed
            pass
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if not self.in_main:
            return

        attrs = dict(attrs)
        el_id = attrs.get("id")
        if el_id:
            self.id_stack.append(el_id)
            self.current_id = el_id

        anchor = el_id or self.current_id or self.page

        if tag in HEADING_TAGS:
            self.push("heading", tag, anchor)
            self.awaiting_lead = True
        elif tag == "dt":
            self.push("dt", tag, anchor)
        elif tag in BLOCK_TEXT_TAGS and self.capture is None and self.awaiting_lead:
            self.push("text", tag, anchor)

    def handle_startendtag(self, tag, attrs):
        # self-closing tags (e.g. <img>) carry no text and no state
        pass

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
            return
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth or not self.in_main:
            # closing an element whose id we pushed (tracked below)
            if self.id_stack and tag in ("div", "section", "article", "table", "dl", "figure", "aside", "ol", "ul"):
                pass
            return

        if self.capture:
            text = html.unescape(clean("".join(self.buffer)))
            if self.capture == "heading":
                self.heading_text = text
                if self.capture_tag == "h1":
                    # page title entry points at the page itself
                    self.add(text, "", self.page)
            elif self.capture == "dt":
                self.heading_text = text       # dt term becomes the title
                self.awaiting_lead = True      # its dd becomes the lead text
            elif self.capture == "text":
                if self.heading_text and text:
                    self.add(self.heading_text, truncate(text), self.capture_id)
                self.awaiting_lead = False
            self.capture = None
            self.capture_tag = None

        # pop id stack when a container closes
        if tag in ("div", "section", "article", "table", "dl", "figure", "aside", "ol", "ul", "nav", "header", "footer", "h2", "h3"):
            if self.id_stack:
                self.id_stack.pop()
                self.current_id = self.id_stack[-1] if self.id_stack else self.page

    def handle_data(self, data):
        if self.capture is not None and not self.skip_depth:
            self.buffer.append(data)


def build():
    all_entries = []
    for page in PAGES:
        path = ROOT / page
        if not path.exists():
            print(f"warning: {page} missing, skipped")
            continue
        parser = PageParser(page, GROUP_NAMES[page])
        parser.feed(path.read_text(encoding="utf-8"))
        # page-level entry: title + meta description
        raw = path.read_text(encoding="utf-8")
        m = re.search(r'<meta name="description" content="([^"]+)"', raw)
        desc = m.group(1) if m else ""
        m2 = re.search(r"<title>(.*?)</title>", raw, re.S)
        title = m2.group(1).replace(" — The Open Studio", "") if m2 else GROUP_NAMES[page]
        all_entries.append({"t": html.unescape(clean(title)), "d": html.unescape(clean(desc)), "u": page, "g": GROUP_NAMES[page]})
        all_entries.extend(parser.entries)

    # drop empty-heading noise and dedupe across (u, t)
    final = []
    seen = set()
    for e in all_entries:
        if not e["t"] or e["t"].lower() in ("back to top", "library", "contributing"):
            continue
        key = (e["u"], e["t"].lower())
        if key in seen:
            continue
        seen.add(key)
        final.append(e)

    out = ROOT / "assets" / "js" / "search-data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(final, ensure_ascii=False, indent=1)
    out.write_text(
        "// The Open Studio — search index. GENERATED by tools/build_search_index.py;\n"
        "// regenerate after content edits.\n"
        "var SEARCH_DATA = " + payload + ";\n",
        encoding="utf-8",
    )
    pages = len({e["u"].split("#")[0] for e in final})
    print(f"wrote {out} — {len(final)} entries across {pages} pages")


if __name__ == "__main__":
    build()
