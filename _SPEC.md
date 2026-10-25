# The Open Studio — authoring spec (read fully before writing any page)

A free photography reference library, in the spirit of the sibling project
[The Open Dojo](https://github.com/adineo-cmd/the-open-dojo). The editable
sources are plain HTML in `src/raw/*.html` (one shared stylesheet at
`public/assets/css/site.css`), wrapped one-to-one by `src/pages/*.astro` —
so authoring rules are pure-HTML rules. **No external images, no tracking.**

Tone: warm, precise, plain-spoken reference writing for learners. Original
prose built on factual knowledge. Use em/en dashes like the rest of the site
(“ — ”). Spell numbers in prose where natural. No emoji. No filler.

## Files in this site

| File (src/raw/) | Page |
|---|---|
| `index.html` | Home — the photography front page (do not touch) |
| `genres.html` | Photography genres catalog |
| `profiles.html` | Genre deep-dives |
| `camera.html` | Camera & exposure |
| `composition.html` | Composition |
| `lighting.html` | Light & lighting |
| `editing.html` | Editing & workflow |
| `gear.html` | Gear & optics |
| `terminology.html` | Terminology |
| `glossary.html` | A–Z glossary |
| `history.html` | History of photography |
| `masters.html` | Master photographers |
| `business.html` | Going professional |
| `learning.html` | Learning paths |
| `search.html` | Search (loads `assets/js/search-data.js`) |

## Required page skeleton

Every subpage uses exactly this skeleton. Copy the header and footer
**verbatim** from below; change only:

1. `<title>` and `<meta name="description">`
2. Which nav link carries `class="current" aria-current="page"` (your page's
   top-level section; if your page lives under “More”, mark the *More* link)
3. The `<main>` content

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{Page}} — The Open Studio</title>
  <meta name="description" content="{{One-sentence page description.}}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&family=IBM+Plex+Sans:wght@400;500;600&family=Noto+Serif+JP:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/site.css">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23B26E1E'/%3E%3Ctext x='32' y='44' font-size='36' text-anchor='middle' fill='white' font-family='serif'%3E%E5%86%99%3C/text%3E%3C/svg%3E">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">
        <span class="brand-seal" aria-hidden="true">写</span>
        <span class="brand-text">The Open Studio
          <small>A free photography library</small>
        </span>
      </a>
      <nav class="site-nav" aria-label="Primary">
        <ul>
          <li><a href="index.html">Home</a></li>
          <li class="has-sub">
            <a href="genres.html">Genres</a>
            <ul class="submenu">
              <li class="subhead">By subject</li>
              <li><a href="genres.html#people">People &amp; portraits</a></li>
              <li><a href="genres.html#places">Places &amp; structures</a></li>
              <li><a href="genres.html#nature">Nature &amp; wildlife</a></li>
              <li><a href="genres.html#commercial">Studio &amp; commercial</a></li>
              <li class="subhead">By approach</li>
              <li><a href="genres.html#documentary">Documentary &amp; street</a></li>
              <li><a href="genres.html#artistic">Artistic</a></li>
              <li><a href="genres.html#technical">Technical &amp; scientific</a></li>
              <li class="subhead">Start here</li>
              <li><a href="genres.html#featured">Featured genres</a></li>
              <li><a href="genres.html#choosing">Choosing your genre</a></li>
            </ul>
          </li>
          <li class="has-sub">
            <a href="camera.html">Craft</a>
            <ul class="submenu">
              <li><a href="camera.html">Camera &amp; exposure</a></li>
              <li><a href="composition.html">Composition</a></li>
              <li><a href="lighting.html">Light &amp; lighting</a></li>
              <li><a href="editing.html">Editing &amp; workflow</a></li>
              <li><a href="gear.html">Gear &amp; optics</a></li>
            </ul>
          </li>
          <li><a href="terminology.html">Terminology</a></li>
          <li class="has-sub">
            <a href="masters.html">More</a>
            <ul class="submenu">
              <li class="subhead">Study</li>
              <li><a href="profiles.html">Genre profiles</a></li>
              <li><a href="masters.html">Masters</a></li>
              <li><a href="history.html">History</a></li>
              <li><a href="glossary.html">Glossary</a></li>
              <li class="subhead">Practice</li>
              <li><a href="business.html">Going pro</a></li>
              <li><a href="learning.html">Learning paths</a></li>
              <li class="subhead">Reference</li>
              <li><a href="search.html">Search</a></li>
            </ul>
          </li>
        </ul>
        <form class="searchbox" action="search.html" role="search">
          <input type="search" name="q" placeholder="Search the library…" aria-label="Search the library">
        </form>
      </nav>
    </div>
  </header>

  <main id="main">
    <!-- content starts here: page-hero, then sections -->
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <div class="footer-brand">
          <span class="brand-seal" aria-hidden="true">写</span>
          <strong>The Open Studio</strong>
        </div>
        <p>A free, community-minded reference for photographers of every level — genres, craft, light, editing, history, and the business of shooting, written to be read between sessions.</p>
      </div>
      <div>
        <h4>Library</h4>
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
        </ul>
        <h4>Contributing</h4>
        <ul>
          <li><a href="mailto:editors@openstudio.example">Send a correction</a></li>
          <li><a href="mailto:editors@openstudio.example">Suggest a genre</a></li>
        </ul>
        <p class="small">Found a mistake? These pages improve the way negatives do — repetition with attention.</p>
      </div>
    </div>
    <div class="footer-legal">
      <div class="container">
        <span>© 2026 The Open Studio. Original reference content, written for people who make things.</span>
        <span>Informational only — respect privacy, permits, and wildlife when you shoot.</span>
      </div>
    </div>
  </footer>
</body>
</html>
```

## Content conventions

- Open `<main>` with a **page hero**:

```html
<div class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Library</a> → Your Page</p>
    <h1>Page title</h1>
    <p class="lede">Two or three sentences: what this page covers and who it's for.</p>
    <nav aria-label="Jump to">
      <ul class="jump-list">
        <li><a href="#section-id">Section</a></li>
        <!-- one per major section -->
      </ul>
    </nav>
  </div>
</div>
```

- Then `<section class="section-tight"><div class="container">…</div></section>`
  blocks, one per major topic, each with `<h2>` and optional
  `<p class="section-intro">`.
- Long groups use `<div class="group-block">` with an `<h3>` heading
  (optional `<span class="group-note">context</span>` inside the h3).
- Vocabulary/definition pairs use `<dl class="term-grid">` (dt/dd pairs).
- Tables: wrap in `<div class="table-wrap">`, use `<table class="wiki">`,
  `<th scope="col">` headers, `class="num"` for numeric cells, `class="jp"`
  for kanji.
- Skill-level indicators in tables: `<span class="level-dot l-1"></span>`
  (l-1 beginner → l-5 advanced) followed by the label text. Add an
  `.anchor-note` legend under the first table that uses them.
- Chips: `<span class="chip chip-subject">People</span>` — variants
  `chip-subject` (people/subjects), `chip-approach` (method/approach),
  `chip-place` (location-based), `chip-pro` (commercial/professional),
  plain `chip` for neutral tags.
- Cards for genres/people: `<div class="style-grid">` of
  `<article class="style-card">` with `<div class="script">` (a short kanji
  or the name itself), `<div class="origin">`, `<h3>`, `<p>`, `.chips`,
  optional `<a class="more">`.
- Callouts: `<div class="callout">` (info), `callout--safety` (ethics/legal
  warnings), `callout--plain` (neutral note).
- Side-by-side prose: `<div class="split">` or `split--3` of `<div class="panel">`.
- End long pages with `<p class="anchor-note"><a class="back-top" href="#main">Back to top</a></p>`.
- Cross-link generously to sibling pages (`genres.html#people`,
  `camera.html#aperture`, …) — but ONLY to anchors listed below.
- After editing any page, regenerate the search index:
  `python3 tools/build_search_index.py`.

## Canonical anchors (so cross-links never break)

- `genres.html`: `#featured` `#people` `#places` `#nature` `#commercial` `#documentary` `#artistic` `#technical` `#choosing`
- `profiles.html`: `#portrait` `#landscape` `#street` `#wildlife` `#wedding` `#macro` `#astro` `#food` `#product` `#fashion` `#documentary` `#sports`
- `camera.html`: `#triangle` `#aperture` `#shutter` `#iso` `#stops` `#metering` `#modes` `#focus` `#white-balance` `#histogram` `#raw` `#holding` `#exercises`
- `composition.html`: `#thirds` `#golden` `#leading` `#frames` `#symmetry` `#negative` `#balance` `#depth` `#viewpoint` `#scale` `#patterns` `#color` `#breaking`
- `lighting.html`: `#qualities` `#natural` `#daylight` `#patterns` `#setups` `#modifiers` `#flash` `#mixing` `#keys`
- `editing.html`: `#workflow` `#raw` `#tone` `#color` `#local` `#detail` `#software` `#output` `#backup` `#ethics`
- `gear.html`: `#cameras` `#sensors` `#lenses` `#focal` `#primes` `#support` `#filters` `#flash-gear` `#storage` `#kit`
- `terminology.html`: `#exposure-terms` `#camera-parts` `#lens-terms` `#focus-terms` `#light-terms` `#color-terms` `#output-terms` `#processes` `#abbreviations`
- `glossary.html`: `#a` `#b` `#c` … `#z` (only letters that have entries)
- `history.html`: `#timeline` `#origins` `#film-era` `#color` `#digital` `#movements` `#philosophy`
- `masters.html`: one anchor per photographer id, e.g. `#ansel-adams`
- `business.html`: `#paths` `#portfolio` `#clients` `#pricing` `#contracts` `#rights` `#stock` `#prints` `#marketing` `#mistakes`
- `learning.html`: `#first-year` `#projects` `#drills` `#critique` `#milestones`
- Search: `search.html?q=aperture` must work.

## Accessibility rules

- Every `<img>` needs `alt` (the site uses none by default — keep it that way).
- Kanji decorations are `aria-hidden="true"`.
- Tables need `<th scope="col">`. Definition lists are fine bare.
- No JavaScript except on `search.html`.

## Footer nav “current” marking

- index.html → mark **Home** current
- genres.html → mark **Genres** current
- camera.html, composition.html, lighting.html, editing.html, gear.html →
  mark **Craft** current
- terminology.html → mark **Terminology** current
- every other page (profiles, glossary, masters, history, business, learning,
  search) → mark **More** current
