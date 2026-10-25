# The Open Studio — a free photography reference library

A photography-dedicated reference library in the spirit of
[The Open Dojo](https://github.com/adineo-cmd/the-open-dojo): fifteen pages on
genres, exposure, composition, light, editing, gear, history, masters, the
business of shooting, and learning paths — plus client-side search.

Built with [Astro](https://astro.build) using a passthrough structure: the
editable sources live in `src/raw/*.html` (plain HTML, one shared stylesheet
in `public/assets/css/site.css`), each wrapped by `src/pages/*.astro`.
Deployed to GitHub Pages on every push to `main`.

| Page | Contents |
|---|---|
| `index` | Home — section cards, featured genres, settings spotlight, home-studio guide, reading shelf |
| `genres` | 70+ photography genres catalogued by subject, approach, and place |
| `profiles` | Twelve genres in depth — history, a typical shoot, skills, masters |
| `camera` | The exposure triangle, aperture, shutter, ISO, stops, metering, focus, histograms, RAW |
| `composition` | Thirds, golden ratio, leading lines, frames, negative space, color, breaking the rules |
| `lighting` | Qualities of light, the day's light arc, studio patterns, modifiers, flash, gels |
| `editing` | Workflow, RAW development, tone & color, local edits, software, output, 3-2-1 backup, ethics |
| `gear` | Camera types, sensor sizes, focal lengths, primes vs zooms, support, filters, starter kits |
| `terminology` | Exposure, camera, lens, focus, light, color, print, process vocabulary + abbreviations |
| `glossary` | A–Z glossary — one line per term, from every page |
| `history` | Timeline from camera obscura to computational photography, movements, philosophy |
| `masters` | Fourteen photographers who changed how we see — and what to steal from each |
| `business` | Going pro: paths, portfolio, clients, pricing, contracts, rights, stock, prints |
| `learning` | A first-year curriculum, 52-week projects, drills, critique, milestones |
| `search` | Client-side search over the library's entries |

## Editing

Edit the HTML in `src/raw/`, then regenerate the search index and rebuild:

```bash
python3 tools/build_search_index.py   # writes public/assets/js/search-data.js
npm install
npm run dev                          # local preview
npm run build                         # production build to dist/
```

`_SPEC.md` is the authoring blueprint (skeleton, classes, canonical anchors).

## Notes

- All reference content is original writing built on factual, historical data.
- Informational only — respect privacy, permits, and wildlife when you shoot.
- Sibling project: [The Open Dojo](https://github.com/adineo-cmd/the-open-dojo).
- © 2026 The Open Studio.
