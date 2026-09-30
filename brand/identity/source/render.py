"""Headless-Chrome rendering helpers shared by the identity build scripts (no Python dependencies).

rasterize(): many SVG → PNG/JPG jobs in one Chrome session (canvas.toDataURL), transparent unless a background is set.
pdf():       one SVG → a single-page vector PDF exactly the SVG's size.
screenshot(): one HTML page → a PNG of exactly width × height px. Unlike rasterize() (an SVG drawn through an image,
             which can't load web fonts), this renders a real page, so embedded fonts and images render exactly.
"""

import base64
import html as html_lib
import json
import os
import re
import shutil
import subprocess
import tempfile

CHROME_CANDIDATES = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome")


def chrome_bin():
    for c in [os.environ.get("CHROME")] + list(CHROME_CANDIDATES):
        if c and shutil.which(c):
            return shutil.which(c)
    raise SystemExit("Chrome/Chromium not found. Install it or set CHROME=/path/to/chrome.")


def _chrome(*args, timeout=300):
    return subprocess.run(
        [chrome_bin(), "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def svg_size(svg):
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    return float(m.group(1)), float(m.group(2))


def rasterize(jobs):
    """jobs: list of dicts {svg, out, width, height=None, bg=None, pad=0, fmt='png'|'jpeg'}.
    The SVG is fitted (contain) into width×height minus pad on every side; height defaults to the SVG's aspect."""
    specs = []
    for j in jobs:
        w, h = svg_size(j["svg"])
        W = j["width"]
        pad = j.get("pad", 0)
        H = j.get("height") or round((W - 2 * pad) * h / w + 2 * pad)
        s = min((W - 2 * pad) / w, (H - 2 * pad) / h)
        specs.append(
            {
                "src": "data:image/svg+xml;base64," + base64.b64encode(j["svg"].encode()).decode(),
                "W": W,
                "H": H,
                "x": (W - w * s) / 2,
                "y": (H - h * s) / 2,
                "w": w * s,
                "h": h * s,
                "bg": j.get("bg"),
                "type": "image/" + j.get("fmt", "png"),
            }
        )
    html = """<!doctype html><body><script>
const jobs = __JOBS__;
Promise.all(jobs.map(j => new Promise(done => {
  const img = new Image();
  img.onload = () => {
    const c = document.createElement('canvas'); c.width = j.W; c.height = j.H;
    const x = c.getContext('2d');
    if (j.bg) { x.fillStyle = j.bg; x.fillRect(0, 0, j.W, j.H); }
    x.drawImage(img, j.x, j.y, j.w, j.h);
    done(c.toDataURL(j.type, 0.92));
  };
  img.onerror = () => done('');
  img.src = j.src;
}))).then(r => { document.body.textContent = JSON.stringify(r); });
</script></body>""".replace("__JOBS__", json.dumps(specs))
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    try:
        r = _chrome("--virtual-time-budget=60000", "--dump-dom", "file://" + f.name)
    finally:
        os.unlink(f.name)
    m = re.search(r"<body>(\[.*\])</body>", r.stdout, re.S)
    if not m:
        raise SystemExit("Rendering failed:\n" + r.stderr[-800:])
    urls = json.loads(m.group(1))
    for j, url in zip(jobs, urls, strict=True):
        if not url:
            raise SystemExit(f"Rendering failed for {j['out']}")
        os.makedirs(os.path.dirname(j["out"]), exist_ok=True)
        with open(j["out"], "wb") as fh:
            fh.write(base64.b64decode(url.split(",", 1)[1]))


def pdf(svg, out_path, title="ARANT DESIGN"):
    """Single-page vector PDF at the SVG's own size. `title` becomes the PDF's document title."""
    w, h = svg_size(svg)
    html = (
        f"<!doctype html><title>{html_lib.escape(title)}</title>"
        f"<style>@page{{size:{w}px {h}px;margin:0}}html,body{{margin:0}}"
        f"svg{{display:block;width:{w}px;height:{h}px}}</style>{svg}"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        _chrome("--no-pdf-header-footer", f"--print-to-pdf={out_path}", "file://" + f.name, timeout=120)
    finally:
        os.unlink(f.name)
    if not os.path.exists(out_path):
        raise SystemExit(f"PDF export failed for {out_path}")


def screenshot(html, out_path, width, height):
    """Render a self-contained HTML page (fonts and images embedded as data URIs) to a width × height PNG at device
    scale 1. Virtual time lets embedded fonts load before the capture, so the result is the same on every run."""
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    try:
        _chrome(
            "--force-device-scale-factor=1",
            f"--window-size={width},{height}",
            "--virtual-time-budget=10000",
            f"--screenshot={out_path}",
            "file://" + f.name,
            timeout=180,
        )
    finally:
        os.unlink(f.name)
    if not os.path.exists(out_path):
        raise SystemExit(f"Screenshot failed for {out_path}")


def write_ico(png_paths, out_path):
    """Pack PNG images (e.g. 16/32/48 px) into one .ico file (PNG-compressed entries, supported everywhere current)."""
    blobs = []
    for p in png_paths:
        with open(p, "rb") as fh:
            blobs.append(fh.read())
    header = (0).to_bytes(2, "little") + (1).to_bytes(2, "little") + len(blobs).to_bytes(2, "little")
    entries, offset = b"", 6 + 16 * len(blobs)
    for b in blobs:
        w = int.from_bytes(b[16:20], "big")
        h = int.from_bytes(b[20:24], "big")
        entries += (
            bytes([w % 256, h % 256, 0, 0])
            + (1).to_bytes(2, "little")
            + (32).to_bytes(2, "little")
            + len(b).to_bytes(4, "little")
            + offset.to_bytes(4, "little")
        )
        offset += len(b)
    with open(out_path, "wb") as f:
        f.write(header + entries + b"".join(blobs))
