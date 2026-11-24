#!/usr/bin/env python3
"""Crop source photos to the Frame photo area (1600x1440) as sRGB JPEGs.

Usage: python3 photos/prep_photos.py SRC1.jpg SRC2.jpg SRC3.jpg
Writes photos/frame-1.jpg .. frame-3.jpg. Colour is left untouched: the Frame's
own conversion handles the Spectra 6 palette. Re-encoding drops EXIF/GPS metadata.
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

OUT = Path(__file__).resolve().parent
SIZE = (1600, 1440)
FOCUS = [(0.55, 0.55), (0.50, 0.50), (0.50, 0.50)]  # crop centre (x, y) per photo


def main(paths):
    if len(paths) != len(FOCUS):
        sys.exit(f"Expected {len(FOCUS)} photos, got {len(paths)}")
    w, h = SIZE
    for n, (p, f) in enumerate(zip(paths, FOCUS), 1):
        im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        s = max(w / im.width, h / im.height)
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        x = min(max(round(f[0] * im.width - w / 2), 0), im.width - w)
        y = min(max(round(f[1] * im.height - h / 2), 0), im.height - h)
        im.crop((x, y, x + w, y + h)).save(OUT / f"frame-{n}.jpg", quality=86, optimize=True, progressive=True)


if __name__ == "__main__":
    main(sys.argv[1:])
