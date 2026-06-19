---
name: generar-fotogramas
description: Genera los fotogramas de una transición scroll-down a partir de DOS imágenes (una inicial y una final). Úsalo cuando el usuario aporte dos imágenes y pida los frames/fotogramas para una web scroll-down (sistema v2), o diga "genérame el vídeo en fotogramas" / "interpola estas dos imágenes en frames".
---

# Generar fotogramas a partir de dos imágenes

Convierte dos imágenes (inicial → final) en una secuencia de fotogramas
`frame-001.jpg … frame-NNN.jpg` que reproducen una transición suave, lista para
la carpeta `frames/` del generador de webs scroll-down (v2). No necesita un modelo
de vídeo: interpola localmente con un crossfade suavizado + un ligero zoom.

## Cuándo usar esta skill
- El usuario da **dos imágenes** (inicio y fin) y quiere los **fotogramas** del
  efecto scroll.
- Pide "el vídeo ya en fotogramas", "interpola estas dos imágenes" o "frames para
  la web v2".

## Requisitos
- Python 3 con **Pillow** (`pip install pillow`).

## Cómo ejecutarla
1. Identifica las rutas de las dos imágenes que ha dado el usuario (inicial y final).
2. Pregunta (o asume valores por defecto sensatos) cuántos fotogramas quiere
   (40 es buen valor; 60 más fluido) y el tamaño (1280x720 por defecto).
3. Ejecuta el script incluido `interpolar.py`:

```
python interpolar.py <INICIAL> <FINAL> --frames 40 --out frames --size 1280x720
```

Opciones:
- `-n, --frames N`  → número de fotogramas (def. 40).
- `-o, --out DIR`   → carpeta de salida (def. `frames`).
- `--size WxH`      → resolución (def. 1280x720).
- `--zoom 0.06`     → intensidad del zoom Ken Burns (0 = sin zoom).
- `--quality 88`    → calidad JPG.

4. Informa al usuario de la carpeta generada y dile que copie esos fotogramas a
   `proyectos/<nombre>/frames/` de su proyecto v2 (o a `proyecto/frames/` en modo
   simple) y construya con `python3 construir.py <nombre>`.

## Notas
- El orden importa: la **primera** imagen es el inicio del scroll y la **segunda**
  el final.
- Ambas imágenes se ajustan al mismo tamaño (modo "cover", recorte centrado), así
  que pueden tener proporciones distintas.
- Esto produce una transición tipo disolución con movimiento. Para un efecto más
  cinematográfico (objetos que se mueven, cámara real) conviene un vídeo generado
  con IA (Veo/Kling/Runway/Luma) y trocearlo; esta skill es la vía rápida y
  gratuita cuando solo tienes las dos imágenes clave.
