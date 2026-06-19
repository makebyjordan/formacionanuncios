# `creaciones/` — contenido organizado por marca

Copias estructuradas de las creaciones (imágenes y vídeos) clasificadas por marca. **El original siempre vive en `all/`** (la bandeja de entrada); aquí hay duplicados ordenados.

## Estructura
```
allVideosPhotoIaALL/
  all/                         ← bandeja de entrada: el usuario suelta TODO aquí (logos + creaciones)
  marcas/<slug>/logos/         ← logos por marca
  creaciones/
    <slug-de-marca>/
      imagenes/
      videos/
    _compartido/               ← activos usados en varias marcas (p.ej. la actriz UGC base)
```

## Marcas actuales
- `inteligencia-sevilla/` — consultoría IA (oficina cálida, presentadora + equipo, visitas a clientes).
- `vexa/` — gafas inteligentes (renders de producto, lifestyle en calle, unboxing, reveal de logo).
- `forgenex/` — desarrollo de CRM (UGC en oficina con branding Forgenex).
- `_compartido/` — `avatar-model.mp4` (retrato de la actriz UGC, reutilizada en las tres marcas).

## Flujo "estructura"
1. El usuario vuelca cualquier cosa nueva en `all/` (logos y/o creaciones).
2. El usuario dice **"estructura"**.
3. Claude:
   - Logos nuevos → `marcas/<slug>/logos/` (+ `marca.md` si la marca es nueva).
   - Creaciones nuevas → `creaciones/<slug>/imagenes|videos/` (copia; el original se queda en `all/`).
   - Lo que sirva a varias marcas → `creaciones/_compartido/`.
   - Actualiza `creador anuncios/catalogo-marcas-y-referencias.md`.

## Reglas
- **Nunca se mueve ni borra nada de `all/`** — solo se duplica.
- Clasificación por marca según logo/branding visible, producto o nombre del archivo. Si una pieza es ambigua, Claude pregunta antes de asignarla.

*Última estructuración: 2026-06-18 — 30 piezas (IS 17, VEXA 8, Forgenex 4, compartido 1).*
