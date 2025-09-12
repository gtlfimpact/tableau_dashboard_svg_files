import pathlib, re

WRAPPER_TOP = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{title}</title>
    <style type="text/css">body {{ margin: 0; }}</style>
  </head>
  <body>
"""
WRAPPER_BOTTOM = """
  </body>
</html>
"""

root = pathlib.Path(__file__).resolve().parents[1]
svgs_dir = root / "svgs"
site_dir = root / "site"
site_dir.mkdir(exist_ok=True)

# Try to map inputs like info_card_1.svg ... info_card_9.svg to /info1 ... /info9
# Also accept background.svg or impact_background.svg -> /background
def read_svg(path: pathlib.Path) -> str:
    s = path.read_text(encoding="utf-8")
    # Remove XML prolog if present
    s = re.sub(r'^\s*<\?xml[^>]*\?>\s*', '', s, count=1, flags=re.IGNORECASE)
    return s

# Process info cards
for i in range(1, 10):
    candidates = [
        svgs_dir / f"info_card_{i}.svg",
        svgs_dir / f"info_card_{i:02d}.svg",
        svgs_dir / f"info{i}.svg",
    ]
    chosen = None
    for c in candidates:
        if c.exists():
            chosen = c
            break
    out_dir = site_dir / f"info{i}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    if chosen is None:
        # Leave placeholder if not provided
        out_path.write_text(WRAPPER_TOP.format(title=f"info{i}") + "<!-- missing SVG: place it here -->\n" + WRAPPER_BOTTOM, encoding="utf-8")
        print(f"[warn] missing SVG for info{i}")
    else:
        svg = read_svg(chosen)
        html = WRAPPER_TOP.format(title=f"info{i}") + svg + WRAPPER_BOTTOM
        out_path.write_text(html, encoding="utf-8")
        print(f"[ok] wrote {out_path} from {chosen.name}")

# Process background
bg_candidates = [
    svgs_dir / "background.svg",
    svgs_dir / "impact_background.svg",
    svgs_dir / "main_background.svg",
]
bg_chosen = None
for c in bg_candidates:
    if c.exists():
        bg_chosen = c
        break
bg_dir = site_dir / "background"
bg_dir.mkdir(parents=True, exist_ok=True)
bg_out = bg_dir / "index.html"
if bg_chosen is None:
    bg_out.write_text(WRAPPER_TOP.format(title="background") + "<!-- missing SVG: place it here -->\n" + WRAPPER_BOTTOM, encoding="utf-8")
    print("[warn] missing background SVG")
else:
    svg = read_svg(bg_chosen)
    html = WRAPPER_TOP.format(title="background") + svg + WRAPPER_BOTTOM
    bg_out.write_text(html, encoding="utf-8")
    print(f"[ok] wrote {bg_out} from {bg_chosen.name}")

print("Done. Deploy the 'site/' folder on GitHub Pages.")