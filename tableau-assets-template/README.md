# Tableau SVG Cards static site

This repo hosts 10 URLs for Tableau to pull:
- /info1 ... /info9
- /background

Each URL serves an HTML page with an inline SVG and zero margins.

## Two ways to prepare the pages

### A) No-code paste
1. Open each `site/<name>/index.html` and paste the SVG markup in place of the comment.
2. Remove the XML prolog if present: `<?xml version="1.0" encoding="UTF-8"?>`.

### B) Auto-wrap your SVG files
1. Put your raw SVGs into the `svgs/` folder with names like:
   - `info_card_1.svg` ... `info_card_9.svg`
   - `background.svg` (or `impact_background.svg`)
2. Run:
   ```bash
   python3 scripts/wrap_svgs.py
   ```
3. The script writes wrapped HTML into `site/` automatically.

## Deploy on GitHub Pages
- Push this repo to GitHub.
- Settings → Pages → Build and deployment → Source: "Deploy from branch"; Branch: `main` and folder `/`.
- Your URLs will be:
  - `https://<username>.github.io/<repo>/info1` ... `/info9`
  - `https://<username>.github.io/<repo>/background`