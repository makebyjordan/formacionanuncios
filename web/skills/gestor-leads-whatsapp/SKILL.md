---
name: gestor-leads-whatsapp
description: |
  Gestor de campañas de prospección por WhatsApp conectado al Google Sheet del usuario. Genera leads nuevos verificados, redacta y reescribe mensajes personalizados al estilo de cada comercial, y mantiene el Sheet actualizado leyendo los clientes existentes y añadiendo filas SIN duplicar nunca un negocio ya presente.

  ÚSALA SIEMPRE que el usuario diga: "genérame X leads", "leads nuevos", "más leads", "siguiente tanda", "rehazme/reescribe los mensajes personalizados", "ya acabé la primera tanda", "actualiza/añade a mi Google Sheet de leads", o trabaje con su hoja de prospección (seguros = pestaña sandra, peluquería canina = pestaña jordan, u otros sectores/comerciales nuevos). Cubre a Sandra Delgado y Jordan García y permite añadir comerciales/sectores.

  Orquesta la skill prospector-realtime-empresas para datos reales en vivo y escribe en el Sheet vía navegador. PROHIBIDO inventar empresas o teléfonos y PROHIBIDO duplicar clientes existentes.
---

# Gestor de Leads por WhatsApp (Inteligencia Sevilla)

Campañas de captación por WhatsApp. Trabaja sobre un Google Sheet con **una pestaña por comercial/sector** y hace tres cosas: (A) generar leads nuevos verificados + su mensaje, (B) reescribir/mejorar mensajes existentes, (C) mantener el Sheet (estados, notas, orden).

**Esta skill es autocontenida.** Todo lo necesario está aquí y en `references/`. No improvises el método de escritura: ya está resuelto abajo. La meta es ir **rápido y sin errores** leyendo todo de una vez, investigando en lote y escribiendo en una sola tanda.

## Datos fijos del proyecto

- **Google Sheet (fileId):** `1LI9DNodTNW7joOf1-1Sn3v3JJ5D7qDXNHJebiytOwxs`
- **URL:** `https://docs.google.com/spreadsheets/d/1LI9DNodTNW7joOf1-1Sn3v3JJ5D7qDXNHJebiytOwxs/edit`
- **Empresa:** Inteligencia Sevilla — `inteligenciasevilla.com/crms.html`
- **Producto:** CRM / herramienta de gestión **a medida** (fichas, recordatorios, vencimientos, seguimiento), ampliable a futuro.

### Comerciales y pestañas

| Pestaña | Comercial (firma) | Sector | Tono |
|---|---|---|---|
| `sandra` | **Sandra Delgado** | Corredurías / agencias de seguros | Profesional, conciso; cartera, vencimientos, siniestros. **1 párrafo compacto.** |
| `jordan` | **Jordan García** | Peluquerías / estética / guardería canina | Cercano, entusiasta; fichas por mascota, recordatorios, fidelización. **Mensaje largo con saltos de párrafo + coletilla web + despedida + firma.** |

Se pueden **añadir comerciales/sectores nuevos** (ver final). Detalle de voz y plantillas en `references/estilo-mensajes.md`.

> ⚠️ Apertura y cierre del mensaje = **el MISMO comercial**. Nunca mezclar nombres.

---

## ⚠️ Reglas de oro (innegociables)

1. **NUNCA inventar datos.** Nombre, teléfono, web, redes, puntuación y el detalle del gancho salen de **búsqueda real en vivo** (skill `prospector-realtime-empresas` + Claude in Chrome). Si el navegador no responde, **detente y pídelo**.
2. **NUNCA duplicar.** Lee la pestaña ANTES de añadir y deduplica por **nombre y teléfono** (ver "Deduplicación").
3. **Pestaña correcta** según sector: seguros → `sandra`, peluquería canina → `jordan`, sector nuevo → su pestaña.
4. **Formato exacto** de las 14 columnas (abajo).
5. **Confirmar antes de escribir.** Muestra la tabla/los cambios y espera un "sí".
6. **Estilo del comercial** correcto (`references/estilo-mensajes.md`), basado en un **detalle real concreto**.
7. **Verificar al terminar**: inicio y fin de cada celda limpios (sin texto pegado ni erratas de autocompletado tipo "Sevillala"/"Sevillaa").

---

## Esquema de columnas (14, orden físico A→N EXACTO)

| Col | Cabecera | Contenido | Formato real |
|---|---|---|---|
| **A** | Comunidad Autónoma | `Andalucía`, `Región de Murcia`, `Extremadura`, `Castilla-La Mancha`… | Nombre oficial |
| **B** | Provincia | `Sevilla`, `Murcia`, `Badajoz`, `Albacete`, `Toledo`… | |
| **C** | Ciudad | `Sevilla`, `Murcia`… | |
| **D** | Tanda | `Ronda 1`, `Ronda 2` | Ver "Tandas" |
| **E** | Fecha de Envío | **Vacía al crear** | La rellena el usuario al enviar |
| **F** | Nombre del Negocio | Nombre comercial real | Clave de dedupe |
| **G** | Teléfono | Móvil (preferente) o fijo | **Solo dígitos**, sin espacios ni +34 (ej. `634465885`) |
| **H** | Mensaje Personalizado | Texto WhatsApp completo, multilínea | Estilo del comercial; párrafos separados por línea en blanco |
| **I** | Estado actual | `Pendiente` por defecto | También `Enviado`, `Respondido`, `No interesado`, `Reunión` |
| **J** | Sitio Web | `https://…` o vacío | Suele ir también mencionada en Notas |
| **K** | Instagram | handle/URL o vacío | Frecuentemente vacío |
| **L** | Facebook / Otra Red | handle/URL o vacío | Frecuentemente vacío |
| **M** | Puntuación Google Maps | `5.0 (174)` | **Punto** decimal + nº reseñas entre paréntesis, tal cual Maps |
| **N** | Notas / Historial | Tipo de tel., contacto, dirección, especialidad | Ej. `Móvil WhatsApp. C. José María Pemán 4. Caniche, productos Artero` |

> Cabeceras en **fila 1**. Datos desde **fila 2**. Un negocio = una fila.

---

## Flujo rápido (por defecto)

1. **Identifica tarea + pestaña + zona** en una línea. Si es ambiguo, **una sola** pregunta (usa botones).
   - "5 leads de cada ciudad" = 5 por CADA ciudad (no 5 en total). Si dice "ciudades de provincia / capitales", aclara cuáles y cuántas con UNA pregunta antes de empezar (evita el malentendido clásico).
2. **Lee el Sheet de una vez** con el conector de Drive (`read_file_content` sobre el fileId) → construye la **lista de exclusión** (Nombre + Teléfono) y localiza la **última fila** y el nº de fila de cada negocio. (El conector es **solo lectura**; se escribe por navegador.)
3. **Investiga en vivo y en lote** (`prospector-realtime-empresas`): por ciudad, abre Maps, saca de cada candidato puntuación, nº reseñas, teléfono (prioriza móvil), web/IG y **1–2 detalles reales** de reseñas para el gancho. Deduplica sobre la marcha. Sigue buscando hasta completar el número pedido tras descartar duplicados.
4. **Redacta TODOS los mensajes** con el estilo del comercial (`references/estilo-mensajes.md`).
5. **Muestra la tabla completa** (14 columnas) y **pide confirmación** una sola vez.
6. **Escribe en una tanda** con el método fiable (abajo y en `references/conexion-sheets.md`). **Verifica** celda a celda al final.
7. Si trabajas por ciudades, ve **ciudad por ciudad** (muestra→confirma→escribe) para no acumular errores, pero dentro de cada ciudad haz todo del tirón.
8. Cierra: *"✓ Añadidos N leads a `jordan`. Total: M filas."*

Para reescribir mensajes (TAREA B) o mantenimiento (TAREA C), ver detalle abajo.

---

## ⚠️ ESCRITURA EN EL SHEET — método probado (NO improvisar)

La lectura es por conector de Drive. **La escritura es por navegador (Claude in Chrome).** Comprueba que la extensión está conectada (`tabs_context_mcp`). Si no responde, **detente y pídela** (no fuerces).

### Antes de escribir (setup que ahorra tiempo)
- **Agranda la ventana** (`resize_window` ~1600×1240). Con la ventana ancha se ven todas las columnas A→N y el cuadro de nombres y los clics funcionan mucho mejor. Casi todos los fallos de posicionamiento vienen de ventana estrecha.
- **Tras un `navigate` que recarga el Sheet**, primero **clic en una celda de datos** (p. ej. fila 2) para devolver el foco a la cuadrícula; solo entonces usa atajos. Si haces atajos nada más cargar, el foco está en A1 y fallan.
- **Localiza la primera fila vacía** así: clic en una celda de datos real → `Cmd+Down` (salta a la última con datos) → `Down` (primera vacía). No te fíes de números de fila a ojo.

### MÉTODO A — PRINCIPAL (rápido): pegado en bloque por portapapeles (TSV)
Escribe varias celdas/filas de golpe con **un solo `Cmd+V`**. Respeta saltos de línea dentro de celda. Es el más rápido y fiable.

1. Sitúa la celda de inicio del bloque (p. ej. `A<fila>`). Para ir exacto, clic en cuadro de nombres → teclea la celda → Return (solo para **navegar**, nunca para escribir contenido). Si el cuadro de nombres no engancha (ventana estrecha), agranda ventana o usa `Cmd+Up`/`Cmd+Down` + flechas.
2. Construye el contenido como **TSV**: columnas separadas por **TAB** real, filas por salto de línea. Cada celda con **saltos internos** (los mensajes) va **entre comillas dobles** y sus saltos como `\n`; comillas internas duplicadas (`""`).
3. Pon el TSV en el portapapeles y pega:
   - Con JS: `await navigator.clipboard.writeText(tsv)` y luego `computer` → tecla `Cmd+V`.
   - Sheets reparte TAB=columna y comillas=celda multilínea, hacia la derecha y abajo desde la celda activa.
4. Para reescribir solo mensajes (TAREA B) el bloque es **una columna** (H). Filas contiguas → un pegado; no contiguas → un `H<fila>` + `Cmd+V` por mensaje.

> Si el pegado en bloque falla en este entorno, usa el Método B sin perder tiempo.

### MÉTODO B — RESCATE fiable: tecleo celda a celda
Reglas duras aprendidas (NO repetir errores):
- **NUNCA metas `\t` dentro de un `type`**: en este Sheets el tab embebido NO cambia de columna, lo interpreta como contenido y **apila TODO en la columna A**. Para cambiar de columna pulsa **`Tab` como acción `key` independiente** entre cada valor.
- **NUNCA metas `\n` dentro de `type`** para los párrafos del mensaje.
- **Para la celda del mensaje (H):** entra en edición con **`F2`**, escribe el párrafo, y entre párrafos pulsa **`alt+Return`** (y `alt+Return` doble si quieres línea en blanco visible). Sin F2 previo, el primer `alt+Return` a veces NO inserta salto y el texto sale pegado: si lo ves pegado, **rehaz la celda con F2**.
- **Evita el autocompletado de Sheets** (causa "Sevillala"/"Sevillaa"): tras escribir la última línea de una celda, pulsa **`Delete`** (rechaza la sugerencia) **antes** del `Tab`/`Return` final. Si aun así aparece una letra extra al final, corrígelo: `F2` → `Cmd+Down` → `End` → `BackSpace` → `Return` (sin `Escape`, que descarta la edición).

Secuencia por fila (Método B), partiendo en `A<fila>` vacía:
`type A` → `Tab` → `type B` → `Tab` → `type C` → `Tab` → `type "Ronda 1"` → `Tab` → `Tab` (salta E vacía) → `type F(nombre)` → `Tab` → `type G(teléfono)` → `Tab` → (en H) `F2` → mensaje con `alt+Return` → `Delete` → `Tab` → `type "Pendiente"` → `Tab` ×3 (salta J,K,L o rellénalas si hay web/IG) → `type M(puntuación)` → `Tab` → `type N(notas)` → `Delete` → `Return`.

### MÉTODO C — si no hay navegador
Entrega las filas como **TSV/tabla listas para pegar** y avisa de que se escribirán al reconectar.

### Verificación final (siempre)
- Lee de nuevo con el conector de Drive **o** revisa por la barra de fórmulas: cada celda H empieza con el saludo correcto y **termina** en la firma limpia del comercial (sin "la"/"a" extra).
- Confirma que la última fila con datos es la esperada (no se duplicó ni se desplazó nada).
- Busca erratas: `Cmd+F` → `Sevillala` y `Sevillaa` deben dar **0** resultados.

---

## Ordenar la pestaña por Provincia/Ciudad (agrupar bloques)

Cuando el usuario quiera los leads agrupados:
1. Selecciona **todo el bloque con cabecera** `A1:N<última>` (`Cmd+Up`+`Cmd+Left` para ir a A1, luego `Cmd+Shift+Down`+`Cmd+Shift+Right`).
2. Menú **Datos → Ordenar intervalo → Opciones avanzadas de ordenación de intervalos**. Para llegar fiable a esa opción, abre Datos, baja con flechas a "Ordenar intervalo", `Right` para el submenú, baja a "Opciones avanzadas", `Return`. (Un clic directo en el submenú suele ejecutar el orden simple A→Z; si pasa, **`Cmd+Z`** y reintenta por teclado.)
3. En el diálogo: **marca "Los datos tienen una fila de encabezado"** (¡imprescindible, o mueve la cabecera!), ordena por **Columna A** (Comunidad), añade **Columna B** (Provincia) y **Columna C** (Ciudad), y pulsa **Ordenar**.

---

## TAREA A — Generar leads nuevos
Sigue el "Flujo rápido". Estado `Pendiente`, Fecha de Envío vacía, Tanda = ronda en curso.

## TAREA B — Reescribir / mejorar mensajes (con investigación en vivo SIEMPRE)
> Decisión del usuario: al reescribir, **siempre** investigar web + redes + reseñas en vivo (no solo las Notas), para personalizar más.
1. Identifica clientes/pestaña; localiza cada uno por *Nombre del Negocio* y anota su **nº de fila** (para `H<fila>`).
2. **Investiga cada negocio en vivo**: web, IG/FB, reseñas Maps → 1–2 detalles nuevos concretos. Si encuentras web/redes/puntuación que faltaban, prepáralas para actualizar sus columnas.
3. **Reescribe** con estilo del comercial + detalle real; aplica indicaciones ("más corto", "más directo"…).
4. Muestra **antes / después** y **pide confirmación**.
5. Actualiza la **columna H** (y J/K/L/M si las verificaste) con Método A; filas no contiguas → un pegado por celda. **No toques otras columnas.**
6. **Verifica** inicio/fin limpios.

## TAREA C — Mantenimiento del Sheet
Marcar enviados, cambiar Estado, añadir Notas, registrar respuestas: localiza filas por nombre, muestra el cambio, confirma, escribe la(s) celda(s) concretas, verifica.

---

## Deduplicación (crítico)
- **Teléfono**: normaliza (sin espacios, guiones, `+34`/`0034`). Igual = duplicado.
- **Nombre**: minúsculas, sin tildes, sin `S.L.`/`Correduría`/`Peluquería`… Equivalente = duplicado.
- Ante la duda → duplicado (descártalo). Aplica dedupe **también entre los leads nuevos** de la tanda.
- Si faltan leads, **sigue buscando en vivo**; nunca rellenes con duplicados ni inventes.

## Tandas / rondas
Misma zona tras acabar una tanda → `Ronda N+1`. Zona nueva → normalmente `Ronda 1` de esa zona. Si hay duda, pregunta.

## Añadir un comercial/sector nuevo
Pregunta: nombre del comercial (firma), sector, tono y nombre de pestaña. Crea (o pide crear) la pestaña con las **14 columnas**. Añade su perfil de voz al patrón de `references/estilo-mensajes.md`. Luego opera igual.

## Control de calidad del mensaje (checklist antes de escribir)
- [ ] Apertura y cierre = **mismo comercial**.
- [ ] **Detalle real y concreto** del negocio (no genérico): puntuación/reseñas, especialidad, contacto, servicio.
- [ ] Estructura del comercial correcta (jordan: gancho → bloque "a medida + ampliable" → auditoría gratis → pregunta → coletilla web → despedida → firma. sandra: 1 párrafo con gancho + valor + auditoría + pregunta + firma en línea).
- [ ] Cierre con pregunta. Firma sin erratas.
- [ ] "tú" si hay nombre de persona; "vosotros" si es equipo/negocio.
- [ ] Sin duplicar cliente existente.

## Referencias
- `references/estilo-mensajes.md` — Voz y plantillas por comercial, con ejemplos aprobados.
- `references/conexion-sheets.md` — Lectura/escritura sin romper formato, métodos por prioridad y dedupe técnico.
- Skill relacionada: **`prospector-realtime-empresas`** — motor de búsqueda real en vivo (la invoca la TAREA A y B).
