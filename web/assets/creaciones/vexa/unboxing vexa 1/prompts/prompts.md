# Prompts — Unboxing VEXA 1

- **Set:** unboxing vexa 1
- **Marca:** VEXA (gafas inteligentes con IA)
- **Flujo:** Fotos de referencia → vídeo de unboxing (Google Flow / Veo, 9:16) + imágenes de producto con logo
- **Fecha:** sesión "Unboxing video prompt"

Contexto: anuncio de unboxing de las gafas VEXA — manos abriendo una caja negra mate con el logo VEXA (emblema alado azul "VF" + wordmark "VEXA" + "AI SMART GLASSES"), sacando las gafas blancas mate de lentes espejadas rojo-naranja. Audio solo ambiente, sin música ni voz. Las referencias de imagen del set están en `referencias PRO para video/unboxing vexa 1/` (fotos 1-11) y los vídeos generados en `videos/unboxing vexa 1 video/`.

---

## Vídeo unboxing · 9:16 — versión inicial (con logos integrados)

```
Vertical 9:16 cinematic unboxing video, single continuous handheld POV shot from above looking down at a white table. Soft natural indoor lighting, shallow depth of field, realistic textures. A pair of hands slowly unboxes a premium matte black product box. On the lid is the brand logo: a glowing blue gradient winged "VF" emblem above the wordmark "VEXA" in clean black letters, with the small tagline "AI SMART GLASSES" underneath. The hands lift the magnetic lid, revealing an orange interior tray. They take out a black drawstring fabric pouch, loosen the cord, and slide out a pair of modern smart sunglasses: matte white frames with vivid red-to-orange mirrored lenses and tiny speaker holes near the hinges. On the side temple of the glasses, the same blue winged "VF" emblem is printed/engraved as a small brand mark. The hands turn the glasses gently to catch the light on the reflective lenses and to show the logo on the temple, then set them down. They also reveal the USB magnetic charging cable and a small warranty card inside the tray. Smooth, calm pacing. Macro detail on the lenses, the frame, and the logos. No people speaking, no faces, only hands. Aspect ratio: 9:16 vertical. AUDIO: ambient diegetic sound only — the soft crinkle of plastic wrap, cardboard sliding, the magnetic lid clicking, the fabric pouch rustling, the light tap of the glasses on the table, gentle hand movements. Quiet room tone. NO music, NO voiceover, NO narration, NO sound effects added — only the natural sounds of the unboxing itself.
```

Nota de ajuste: este prompt completo NO funcionaba bien en Flow — mete 5-6 acciones en un clip de ~8s y Veo lo ignora o lo rechaza. Usar la versión corta (Opción A) o, mejor, los 3 clips encadenados (Opción B) de abajo. Subir los dos PNG de logo como imágenes de referencia, porque Veo deforma texto/símbolos pequeños.

---

## Vídeo unboxing · 9:16 — Opción A (clip único, ~8s, formato Flow)

> Reescritura para que Flow lo digiera: escena única, una acción clara, frase de cámara + frase de audio separada. (El prompt corto exacto quedó guardado en el archivo de la sesión; estructura: "Vertical 9:16" al inicio + una sola acción + línea de audio "ambient diegetic sound only — … NO music, NO voiceover".)

Nota de ajuste: una acción por clip, 3-5 frases, "Vertical 9:16" al inicio, línea de audio separada (solo sonido ambiente).

---

## Vídeo unboxing · 9:16 — Opción B (RECOMENDADA: 3 clips encadenados)

> 3 clips, una sola acción cada uno, repitiendo siempre el bloque de audio ambiente:
> 1. Abrir la caja (manos levantan la tapa magnética → bandeja naranja).
> 2. Sacar las gafas de la funda (aflojar el cordón → deslizar las gafas blancas).
> 3. Macro de marca y lentes (giro de la mano mostrando el emblema en la patilla y las lentes espejadas).

Nota de ajuste: encadenar los 3 clips de ~8s repitiendo el bloque de audio. Reglas: "Vertical 9:16" al inicio de cada clip + línea de audio "ambient diegetic sound only … NO music, NO voiceover".

---

## Imagen · producto con logo en la patilla (misma posición)

> Se pasa a la IA: foto 11 (las gafas) como Imagen 1 + el emblema alado azul "VF" como Imagen 2.

```
Use Image 1 (the white-framed sunglasses with red-orange mirrored lenses) as the base.
Use Image 2 (the blue winged "VF" emblem) as a logo.

Place the blue winged emblem from Image 2 onto the side temple (arm) of the
sunglasses, near the hinge, as a small printed/engraved brand mark. Keep the
emblem's exact shape, blue gradient and glow. Make it follow the angle and
curve of the temple realistically, with correct perspective, lighting and a
subtle reflection on the glossy white frame.

Keep everything else from Image 1 identical: same glasses, same white matte
frame, same red-orange mirrored lenses, same background, same lighting and
shadows. Photorealistic, high detail, no other changes.
```

Nota de ajuste: subir las imágenes en el mismo orden que se nombran (Imagen 1 = gafas, Imagen 2 = logo). El emblema queda mejor pequeño, en la patilla cerca de la bisagra.

---

## Imagen · producto con logo en la patilla (nueva posición, ángulo 3/4)

> Se pasa a la IA: foto 11 (las gafas) como Imagen 1 + el emblema alado azul "VF" como Imagen 2.

```
Use Image 1 (the white-framed sunglasses with red-orange mirrored lenses) as
the product reference. Use Image 2 (the blue winged "VF" emblem) as a logo.

Recreate the SAME sunglasses from Image 1 — same matte white frame, same
red-orange mirrored lenses — but in a NEW position: a side / three-quarter
angle that clearly shows the temple (arm) of the glasses, with the temples
open. The temple must be fully visible and in focus.

On that visible temple, near the hinge, place the blue winged emblem from
Image 2 as a small printed/engraved brand mark. Keep the emblem's exact
shape, blue gradient and glow, following the angle and curve of the temple
with correct perspective, lighting and a subtle reflection on the glossy
white frame.

Photorealistic product photo, clean soft studio lighting, shallow depth of
field, neutral background, high detail. Keep the glasses design identical to
Image 1 — only change the camera angle and add the logo on the temple.
```

Nota de ajuste: pide un ángulo lateral / tres cuartos con las patillas abiertas para que la patilla (y la marca) se vean bien, manteniendo idénticas las gafas de la foto 11.

---

## Notas de producción (montaje)

- Los logos los aporta el usuario como PNG: emblema alado azul "VF" (para la patilla) y logo completo "VEXA — AI SMART GLASSES" (para la caja).
- Para fidelidad de logos/texto: subirlos como imágenes de referencia en Flow, o incrustarlos en postproducción si la IA los deforma.
- Audio en TODOS los clips: solo sonido diegético del propio unboxing. Sin música, sin voz en off, sin efectos añadidos.
