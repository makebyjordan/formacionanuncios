# Biblioteca de Prompts

Colección de prompts analizados y archivados por el Prompt Engineer.

---

### 001 — Director de Arte Creativo para Series de YouTube

**Fuente:** La Academy by Gemini — curso de Google España (YouTube)
**Fecha:** 2026-06-14
**Prompt original:**
Eres un director de arte creativo. Usando la investigación adjunta sobre artistas barrocas, genera tres conceptos de series de videos impactantes para YouTube. Para cada una, proporciona un título atractivo, un enfoque original que conecte los hechos históricos con los intereses actuales del público y el mensaje clave de cada serie. Presenta todo en formato de tabla.

**Técnicas identificadas:** asignación de rol profesional creativo, contexto inyectado por documento adjunto, output múltiple con estructura fija (N=3 elementos), anclaje de perspectiva (histórico↔actual), restricción de formato tabla, campos de output explícitos (título + enfoque + mensaje clave)
**Casos de uso:** conceptualización de contenido educativo para redes, conexión de cualquier tema histórico/técnico con audiencias modernas, generación de series temáticas para cualquier plataforma de contenido
**Nota de diseño:** el anclaje "conecta X histórico con intereses actuales del público" es la técnica de mayor valor — obliga al modelo a hacer el puente creativo en lugar de solo listar datos históricos.

---

### 002 — Animación 3D Multi-Referencia para Vídeo (Flow)

**Fuente:** Curso Google Flow (captura de pantalla)
**Fecha:** 2026-06-14
**Herramienta destino:** Google Flow (generación de vídeo con IA)
**Prompt original:**
Utiliza estos tres recursos. Transforma el boceto de la servilleta en una animación 3D de alta fidelidad que recorre el paisaje eslovaco. Olvídate del avión. Aplica coherencia de estilo usando los tonos de color vintage del banner de mi canal y asegúrate de la continuidad de la iluminación para que la posición del sol coincida con la foto de referencia.

**Técnicas identificadas:** multi-referencia con roles asignados por imagen, transformación de medio (boceto 2D→vídeo 3D), exclusión activa de elementos no deseados, anclaje de estilo por imagen de referencia, restricción de coherencia técnica (iluminación/color), criterio físico objetivo (posición del sol)
**Herramientas compatibles:** Google Flow, Runway, Kling, Sora, Pika — cualquier generador de vídeo que acepte imágenes de referencia múltiples
**Casos de uso:** animar ilustraciones o bocetos sobre escenarios reales, intros de canal con identidad visual propia, adaptación de personajes dibujados a entornos fotorrealistas
**Nota de diseño:** asignar un ROL EXPLÍCITO a cada imagen de referencia ("esta imagen = estilo", "esta imagen = escenario", "esta imagen = sujeto") es la técnica de mayor impacto en prompts multimodales para vídeo — elimina ambigüedad sin añadir descripción verbal.
**Debilidad identificada:** no especifica duración, velocidad de movimiento ni punto de inicio/fin del recorrido.

---
