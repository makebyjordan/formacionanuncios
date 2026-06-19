---
name: analiza_nuevos_anuncios
description: Triggers analysis of new ads in allVideosPhotoIaALL when the user requests ANALIZA, updating the web portal, deploying, and pushing to GitHub.
---

# Analizar nuevos anuncios IA

Cuando el usuario pida analizar la carpeta de creaciones, por ejemplo diciendo "ANALIZA":

1. Ejecuta `python3 analiza.py` en la raíz de la carpeta de trabajo `/Users/makebyjordan/local/myweb2teach`.
2. El script comprobará si hay nuevos anuncios (vídeos, imágenes, markdown) que no estén registrados en `web/projects.json`.
3. Para cada nuevo anuncio:
   - Copiará los recursos de la carpeta original a `web/assets/creaciones/`.
   - Generará la página HTML del proyecto en `web/projects/`.
   - Actualizará la base de datos local `web/projects.json`.
   - Hará el despliegue al servidor Hestia a través de `rsync`.
   - Hará git commit y git push al repositorio de GitHub.
4. Muestra un resumen del resultado de la ejecución al usuario.
