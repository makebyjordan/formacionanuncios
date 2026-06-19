# Reglas de Antigravity para este proyecto

## Comando ANALIZA
Cuando el usuario mencione la palabra "ANALIZA" (o variaciones como "analiza", "ANALIZAR", "analizar", "ejecuta el análisis") en su petición, debes:
1. Ejecutar el script `python3 analiza.py` desde la raíz del proyecto (`/Users/makebyjordan/local/myweb2teach`).
2. El script realiza automáticamente las siguientes operaciones si se detectan nuevos anuncios/directorios en `allVideosPhotoIaALL`:
   - Copia los recursos de imagen, vídeo y documentos Markdown al proyecto web.
   - Genera dinámicamente las páginas HTML de detalle para cada nuevo anuncio en `web/projects/`.
   - Agrega la metadata correspondiente a `web/projects.json`.
   - Sincroniza los cambios con el servidor Hestia (usando `rsync` a `jordanstarter.eu`).
   - Sube los cambios al repositorio de GitHub (`https://github.com/makebyjordan/formacionanuncios.git`).
3. Informar al usuario de los resultados obtenidos tras la ejecución del script.
