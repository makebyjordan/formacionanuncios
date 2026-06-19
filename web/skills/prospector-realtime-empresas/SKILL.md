---
name: prospector-realtime-empresas
description: |
  Búsqueda en tiempo real de empresas verificadas de CUALQUIER sector y CUALQUIER ciudad o provincia, para prospección (especialmente WhatsApp).

  Úsalo para encontrar móviles y fijos verificados de empresas con datos 100% reales de fuentes oficiales (Google Maps, webs, avisos legales), cubriendo una ciudad o provincia completa.

  La skill SIEMPRE pregunta primero el sector y la ubicación (es adaptable a todo). FUNCIONA OBLIGATORIAMENTE EN TIEMPO REAL con la extensión Claude in Chrome: abre Google Maps y las webs en el navegador y extrae los datos en vivo. PROHIBIDO inventar o usar datos de memoria. Busca DE 20 EN 20 (sin duplicar), prioriza móviles, verifica cada dato, sugiere sectores relacionados (pero SIEMPRE pregunta), y guarda en el CSV con el formato EXACTO de la plantilla del CRM (plantilla-prospectos.csv), listo para importar.
---

# Prospector Real-Time de Empresas

## ⚠️ REQUISITO OBLIGATORIO: NAVEGACIÓN EN TIEMPO REAL (Claude en Chrome)

**Esta skill SOLO funciona navegando en tiempo real con la extensión de Claude en Chrome (Claude in Chrome).** Es imprescindible y no negociable:

- **OBLIGATORIO** usar las herramientas de **Claude in Chrome** (navigate, read_page, get_page_text, find, computer, etc.) para abrir Google Maps, las webs de las empresas y los avisos legales en el navegador real del usuario.
- **TODOS los datos** (nombre, móvil, fijo, email, web, ubicación) deben extraerse de páginas **abiertas y leídas en vivo** en el navegador, en el momento.
- **PROHIBIDO ABSOLUTAMENTE:**
  - Inventar, suponer o "recordar" empresas o teléfonos de memoria.
  - Rellenar datos sin haberlos visto en pantalla en esa misma sesión.
  - Sustituir la navegación real por conocimiento previo del modelo.
- Cada dato incluido en el Excel debe poder rastrearse a una página concreta que se abrió y leyó con la extensión.

### Comprobación previa OBLIGATORIA

Antes de empezar a buscar, Claude DEBE verificar que la extensión de Claude in Chrome está disponible y conectada:

1. Comprueba que tienes acceso a las herramientas de Claude in Chrome (p. ej. `list_connected_browsers` / `select_browser` / `navigate`).
2. Si **NO** hay ningún navegador conectado, **DETENTE** y di al usuario exactamente esto:
   ```
   ⚠️ No detecto la extensión de Claude en Chrome conectada.
   Esta skill trabaja en TIEMPO REAL navegando por el navegador.
   Por favor:
   1. Instala/activa la extensión "Claude in Chrome".
   2. Abre Chrome y conéctalo a esta conversación.
   Avísame cuando esté lista y empiezo la búsqueda en vivo.
   ```
   **NO inventes datos ni continúes** hasta que la extensión esté conectada.
3. Solo cuando el navegador esté conectado, procede con el flujo de trabajo.

---

## Cuando usar esta skill

Usa esta skill cuando:
- Necesites **prospectar empresas** de **cualquier sector** (asesorías energéticas, fontanería, electricidad, restaurantes, clínicas, abogados, talleres, etc.)
- Busques **teléfonos móviles** para contacto directo por **WhatsApp**
- Requieras **datos verificados** (no inventados) de fuentes oficiales
- Quieras cubrir **cualquier ciudad o provincia** (una localidad concreta o todos los municipios)
- Necesites entrega en **CSV con el formato exacto de tu plantilla de CRM** (`plantilla-prospectos.csv`), lista para importar

Esta skill es **totalmente adaptable**: NO está limitada a ningún sector ni a ninguna geografía. Funciona igual para "fontaneros en Bilbao" que para "clínicas dentales en toda la provincia de Valencia".

---

## Flujo de trabajo

### 1️⃣ CAPTURA DE INTENCIÓN (PRIMER PASO OBLIGATORIO)

**Antes de hacer NADA, pregunta SIEMPRE estas dos cosas. No empieces a buscar sin tener ambas respuestas:**

1. **Sector / actividad:** ¿Qué tipo de empresa o sector buscas?
   - Es válido **cualquier** sector o actividad (ej: "Asesorías energéticas", "Fontanería", "Restaurantes", "Clínicas veterinarias", "Despachos de abogados", "Talleres mecánicos"...).

2. **Ubicación:** ¿En qué ciudad o provincia?
   - Es válida **cualquier** ubicación (ej: Sevilla, Madrid, Bilbao, un pueblo concreto, o toda una provincia).
   - Aclara el alcance: **¿solo una ciudad/municipio o toda la provincia?**
   - Si elige provincia entera: "Buscaré en todos los municipios. Si el navegador se satura, te pediré un PDF con los nombres de municipios para ser más preciso."

Si el usuario no da uno de los dos datos, **pregúntalo explícitamente antes de continuar.** No asumas sector ni ubicación.

### 2️⃣ SUGERENCIA DE SECTORES RELACIONADOS

Una vez tengas sector + ubicación, **sugiere sectores complementarios** adaptados al sector que haya pedido y PREGUNTA si quiere añadirlos. Genera las sugerencias dinámicamente según el sector indicado (no uses una lista fija).

```
Veo que buscas: "<SECTOR DEL USUARIO>" en "<UBICACIÓN DEL USUARIO>"

Sectores relacionados que puedo buscar juntos:
- <relacionado 1>
- <relacionado 2>
- <relacionado 3>

¿Quieres que los añada también? (Sí/No)
```

**Importante:** No añadas sectores sin pregunta explícita.

### 3️⃣ BÚSQUEDA DE 20 EN 20 (SIEMPRE NAVEGANDO EN VIVO)

**PROHIBIDO inventar o duplicar datos. Todo se extrae navegando en tiempo real con Claude in Chrome.**

Para cada bloque de 20 empresas:

1. **Abre Google Maps en el navegador** (`navigate`) y busca el sector + municipio/provincia. Lee los resultados con `read_page` / `get_page_text`.
2. Extrae de la pantalla: Nombre, Móvil, Fijo, Ubicación
3. **Verifica cada dato abriendo las páginas en el navegador (en vivo):**
   - Ficha de Google Maps oficial ✓ (abierta y leída)
   - Página web de la empresa ✓ (abierta con `navigate` y leída)
   - Aviso legal / Política privacidad ✓ (abierto y leído)
   - LinkedIn (si hay) ✓
   - Redes sociales oficiales (si hay) ✓

   Si no puedes abrir y leer la fuente en el navegador, el dato **NO** se incluye.

4. **Prioridad en teléfonos:**
   - ✅ **Móvil verificado** → Incluir SIEMPRE (máxima prioridad)
   - ✅ **Fijo verificado + Email verificado + Web verificada** → Incluir (pero exigir verificación muy rigurosa)
   - ❌ **Solo fijo sin web/email** → NO incluir (no hay forma de contactar por WhatsApp)
   - ❌ **Datos no verificados** → NUNCA incluir

5. Si después de 20 empresas **no hay más:**
   ```
   ✓ Búsqueda completada: 47 empresas encontradas
   ✗ No hay más empresas en base de datos. Pasamos a compilación de Excel.
   ```

### 4️⃣ COMPILACIÓN DE DATOS (FORMATO PLANTILLA CRM — OBLIGATORIO)

**El resultado se guarda EXACTAMENTE en el formato de la plantilla del CRM del usuario** (`plantilla-prospectos.csv`, incluida junto a esta skill). No inventes columnas ni cambies el orden.

**Archivo:** CSV codificado en **UTF-8** (con tildes y ñ correctas), separador coma `,`, valores con comas/saltos entre comillas dobles `"`.

**Cabecera EXACTA (12 columnas, en este orden):**

```
tipo,nombre,empresa,movil,fijo,email,direccion,provincia,sitio_web,sector_sugerido,etiquetas,notas
```

**Reglas por columna:**

| Columna | Qué va | Notas |
|---|---|---|
| `tipo` | `COMPANY`, `PERSON` o `FREELANCER` | En mayúsculas. Empresa → COMPANY; persona individual → PERSON; autónomo/profesional → FREELANCER |
| `nombre` | Nombre de contacto o del negocio | Obligatorio |
| `empresa` | Razón social / nombre comercial | Vacío si es PERSON sin empresa |
| `movil` | Móvil verificado | Solo dígitos o formato tal cual de la fuente. Vacío si no hay |
| `fijo` | Fijo verificado | Vacío si no hay |
| `email` | Email verificado en web/aviso legal | Vacío si no verificado |
| `direccion` | Dirección de Google Maps | Entre comillas si lleva comas |
| `provincia` | Provincia | |
| `sitio_web` | URL completa con `https://` | Vacío si no hay |
| `sector_sugerido` | Sector en formato jerárquico `Categoría > Subcategoría` | Ej: `Hostelería > Restaurantes` |
| `etiquetas` | Etiquetas separadas por `\|` (barra vertical) | Ej: `Caliente\|Referido`. Vacío si no aplica |
| `notas` | Notas libres | Entre comillas si lleva comas |

**Prioridad de inclusión (igual que antes):** Móvil verificado > Fijo+Email+Web verificados. Nunca incluir solo fijo sin web/email, ni datos no verificados.

Ejemplo de filas válidas (formato real de la plantilla):

```
tipo,nombre,empresa,movil,fijo,email,direccion,provincia,sitio_web,sector_sugerido,etiquetas,notas
COMPANY,"Restaurante Tío Pepe","Tío Pepe SL",600111222,911002233,reservas@tiopepe.com,"Calle Mayor 10, Sevilla",Sevilla,https://tiopepe.com,"Hostelería > Restaurantes",Caliente|Referido,"Mesa amplia, eventos"
FREELANCER,"Carlos Vega","Carlos Vega Coach",622555666,,carlos@vegacoach.es,,Málaga,https://vegacoach.es,"Servicios > Marketing y publicidad",,"Quiere demo el próximo viernes"
```

### 5️⃣ GENERACIÓN DE ARCHIVOS

Entrega el resultado **listo para subir al CRM**, respetando la plantilla:

1. **`prospectos_CRM.csv`** → archivo principal en el formato de la plantilla (las 12 columnas exactas de arriba). **Este es el que el usuario sube al CRM.**
   - UTF-8, separador coma, comillas dobles donde haga falta, misma cabecera y mismo orden de columnas que `plantilla-prospectos.csv`.
   - PROHIBIDO añadir, quitar o renombrar columnas.

2. (Opcional, solo si el usuario lo pide) un segundo CSV/Excel de revisión interna. **El entregable por defecto es únicamente el CSV con el formato del CRM.**

Para construirlo de forma fiable, usa la plantilla incluida como base de cabecera y escribe las filas con una librería CSV (p. ej. Python `csv`) para que el escapado de comillas y la codificación UTF-8 sean correctos.

---

## Verificación de datos (CRITICA)

✅ **Móvil verificado:** Google Maps + Web oficial  
✅ **Fijo verificado:** Google Maps + Web oficial + Email  
✅ **Email verificado:** En web oficial o aviso legal (NO asumir)  
✅ **Web verificada:** Que exista y tenga info de la empresa  

❌ **PROHIBIDO:** Inventar, duplicar, asumir emails sin verificación, incluir solo fijos sin email/web, **usar datos de memoria del modelo o cualquier dato no extraído navegando en vivo con Claude in Chrome.**

---

## Flujo de conversación (ejemplo)

```
Usuario: Quiero prospectar empresas

Claude:
Perfecto. Antes de empezar necesito dos datos:

1. ¿Qué sector o actividad buscas? (cualquier sector vale)
2. ¿En qué ciudad o provincia? ¿Solo una ciudad o toda la provincia?

[Usuario: Fontaneros en toda la provincia de Valencia]

Claude:
✓ Entendido: Fontanería en la provincia de Valencia (todos los municipios)

Veo estos sectores relacionados:
- Instaladores de calefacción
- Instaladores de gas
- Reformas de baños

¿Quieres que los añada? (Sí/No)

[Usuario: No]

Perfecto. Buscando de 20 en 20...

📍 Bloque 1 (1-20): Valencia capital
✓ 20 empresas encontradas

📍 Bloque 2 (21-40): Torrent
✓ 18 empresas encontradas

[Continúa...]

✓ BÚSQUEDA COMPLETADA: 156 empresas verificadas

Generando archivo para tu CRM...
📄 prospectos_CRM.csv  (formato exacto de tu plantilla, listo para importar)
```

---

## Plantilla del CRM

Junto a esta skill se incluye `plantilla-prospectos.csv` con la cabecera y filas de ejemplo del CRM del usuario. **Úsala siempre como referencia de formato.** El archivo entregado debe tener la misma cabecera, el mismo orden de columnas y la misma codificación (UTF-8).
