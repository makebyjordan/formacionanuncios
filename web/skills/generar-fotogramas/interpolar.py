#!/usr/bin/env python3
"""Genera los fotogramas de transición de una web scroll-down a partir de DOS
imágenes (inicial y final), sin necesidad de un modelo de vídeo.

Interpola entre ambas con un crossfade suavizado + un ligero zoom (Ken Burns)
para dar sensación de movimiento, y exporta frame-001.jpg ... frame-NNN.jpg
listos para la carpeta `frames/` del sistema v2.

Uso:
    python interpolar.py INICIAL.png FINAL.png --frames 40 --out salida_frames
    python interpolar.py a.jpg b.jpg -n 60 -o frames --size 1280x720

Requiere: Pillow  (pip install pillow)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _cover_resize(img, size):
    """Escala y recorta la imagen para llenar exactamente `size` (modo cover)."""
    from PIL import Image
    tw, th = size
    iw, ih = img.size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - tw) // 2, (nh - th) // 2
    return img.crop((left, top, left + tw, top + th))


def _smoothstep(t: float) -> float:
    return t * t * (3 - 2 * t)


def _zoom(img, factor: float):
    """Zoom centrado (factor >= 1) manteniendo el tamaño del lienzo."""
    from PIL import Image
    if factor <= 1.0:
        return img
    w, h = img.size
    nw, nh = int(w * factor), int(h * factor)
    big = img.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - w) // 2, (nh - h) // 2
    return big.crop((left, top, left + w, top + h))


def main() -> int:
    ap = argparse.ArgumentParser(description="Interpola dos imágenes en fotogramas.")
    ap.add_argument("inicial", help="imagen inicial")
    ap.add_argument("final", help="imagen final")
    ap.add_argument("-n", "--frames", type=int, default=40, help="nº de fotogramas (def. 40)")
    ap.add_argument("-o", "--out", default="frames", help="carpeta de salida (def. frames)")
    ap.add_argument("--size", default="1280x720", help="tamaño WxH (def. 1280x720)")
    ap.add_argument("--zoom", type=float, default=0.06,
                    help="zoom total del efecto Ken Burns (def. 0.06 = 6%)")
    ap.add_argument("--quality", type=int, default=88, help="calidad JPG (def. 88)")
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        print("❌ Falta Pillow.  Instala con:  pip install pillow", file=sys.stderr)
        return 1

    start_p, end_p = Path(args.inicial), Path(args.final)
    for p in (start_p, end_p):
        if not p.is_file():
            print(f"❌ No existe la imagen: {p}", file=sys.stderr)
            return 1

    try:
        w, h = (int(x) for x in args.size.lower().split("x"))
    except ValueError:
        print("❌ --size debe ser WxH, p. ej. 1280x720", file=sys.stderr)
        return 1

    n = max(2, args.frames)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("frame-*.jpg"):
        old.unlink()

    a = _cover_resize(Image.open(start_p).convert("RGB"), (w, h))
    b = _cover_resize(Image.open(end_p).convert("RGB"), (w, h))

    print(f"🎞  Generando {n} fotogramas {w}x{h} en {out}/ …")
    for i in range(n):
        t = i / (n - 1)
        te = _smoothstep(t)
        frame = Image.blend(a, b, te)                 # crossfade suavizado
        frame = _zoom(frame, 1.0 + args.zoom * te)    # ligero zoom progresivo
        frame.save(out / f"frame-{i + 1:03d}.jpg", "JPEG", quality=args.quality)

    print(f"✅ Listo: {n} fotogramas en {out}/ (frame-001.jpg … frame-{n:03d}.jpg)")
    print("   Cópialos a la carpeta frames/ de tu proyecto v2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
