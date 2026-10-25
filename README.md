# The Open Studio — a free photography & crafts reference library

A pure-static, 27-page reference site in the spirit of
[The Open Dojo](https://github.com/adineo-cmd/the-open-dojo) (the martial-arts
library this project is modeled on): no frameworks, no build step, no tracking.
Open `index.html` in a browser and it works — with full wings for photography
**and eleven other fields**: music, cooking & baking, writing, making, visual
arts, performing, programming & design, film & video, gardening, strength &
movement, and languages & translation.

## The library

| Page | Contents |
|---|---|
| `index.html` | Home — section cards, featured genres, settings spotlight, home-studio guide, reading shelf |
| `genres.html` | 70+ photography genres catalogued by subject, approach, and place |
| `profiles.html` | Twelve genres in depth — history, a typical shoot, skills, masters |
| `camera.html` | The exposure triangle, aperture, shutter, ISO, stops, metering, modes, focus, histograms, RAW |
| `composition.html` | Thirds, golden ratio, leading lines, frames, negative space, color, breaking the rules |
| `lighting.html` | Qualities of light, the day's light arc, studio patterns, modifiers, flash, gels |
| `editing.html` | Workflow, RAW development, tone & color, local edits, software, output, 3-2-1 backup, ethics |
| `gear.html` | Camera types, sensor sizes, focal lengths, primes vs zooms, support, filters, starter kits |
| `terminology.html` | Exposure, camera, lens, focus, light, color, print, process vocabulary + abbreviations |
| `glossary.html` | A–Z glossary — one line per term, from every page |
| `history.html` | Timeline from camera obscura to computational photography, movements, philosophy |
| `masters.html` | Fourteen photographers who changed how we see — and what to steal from each |
| `business.html` | Going pro: paths, portfolio, clients, pricing, contracts, rights, stock, prints |
| `learning.html` | A first-year curriculum, 52-week projects, drills, critique, milestones |
| `crafts.html` | The Fields hub — every other wing of the library, and how to build your own |
| `music.html` | Music studio — crafts, practice & ear technique, vocabulary, 8 masters, history, first year, kits |
| `culinary.html` | Cooking & baking studio — knife & heat, balance, baking rules, extraction crafts, masters, kits |
| `writing.html` | Writing studio — scene & story, voice, revision, habits, masters from Austen to Le Guin, kits |
| `making.html` | Making studio — wood, cloth, leather, solder, filament; joinery, finishing, safety, kits |
| `visual-arts.html` | Visual arts studio — drawing, value, color, print & clay; Leonardo to Kahlo, first year |
| `performing.html` | Performing studio — presence, movement, improv, comedy & magic; Graham to Pryor |
| `digital.html` | Digital crafts studio — programming, web, design, games, UX; Lovelace to Torvalds |
| `filmmaking.html` | Film & video studio — directing, cinematography, editing, sound, animation; crew career paths |
| `gardening.html` | Gardening studio — soil, sowing calendar, propagation, design; Brown to Chatto; pro paths |
| `fitness.html` | Strength & movement studio — overload, programming, 80/20 running; Sandow to Kipchoge; coaching careers |
| `languages.html` | Languages & translation studio — input, SRS, shadowing, translator's craft; Mezzofanti to Wilson |
| `search.html` | Client-side search over the library's entries (`assets/js/search-data.js`) |

## Running it

No dependencies. Either open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

Fonts (Source Serif 4, IBM Plex Sans, Noto Serif JP) load from Google Fonts
when online, with system fallbacks offline.

## Notes

- All reference content is original writing built on factual, historical data.
- The ethics note applies everywhere: this is information, not permission —
  respect privacy, permits, and wildlife when you shoot.
- Sibling project: [The Open Dojo](https://github.com/adineo-cmd/the-open-dojo),
  the same library shape for the martial arts.
- © 2026 The Open Studio.
