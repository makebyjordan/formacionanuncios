# Carpeta `marcas/` — estructura y flujo

Esta carpeta guarda los **logos** de cada marca, organizados por marca. Cada marca tiene su propia subcarpeta con esta estructura estándar:

```
marcas/
  _README-estructura.md      ← este archivo
  <slug-de-marca>/
    marca.md                 ← ficha: alias, sector, colores, mundo visual, qué logo usar cuándo
    logos/                   ← todos los archivos de logo de la marca
```

`slug-de-marca` = nombre en minúsculas con guiones (ej. `inteligencia-sevilla`, `vexa`, `forgenex`).

## Marcas actuales
- `inteligencia-sevilla/` — consultoría de IA (IS)
- `vexa/` — gafas inteligentes
- `forgenex/` — desarrollo de CRM

## Flujo para añadir una marca nueva
1. El usuario suelta los archivos de logo de la nueva marca dentro de `marcas/` (sueltos, sin ordenar).
2. El usuario dice: **"analiza la marca que metí"** (o similar).
3. Claude entonces:
   - Detecta los archivos nuevos en la raíz de `marcas/`.
   - Mira cada logo para identificar marca, símbolo y colores.
   - Crea `marcas/<slug>/logos/` y mueve ahí los archivos.
   - Escribe `marcas/<slug>/marca.md` con la ficha.
   - Actualiza `creador anuncios/catalogo-marcas-y-referencias.md` (tabla de reconocimiento + sección de la marca).

## Notas
- El **contenido** (vídeos/fotos de campaña) vive en la carpeta padre `allVideosPhotoIaALL/`, no aquí. Aquí solo logos.
- Mantener el nombre de la marca claro en los archivos ayuda al reconocimiento automático.
