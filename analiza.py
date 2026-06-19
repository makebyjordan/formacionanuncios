import os
import sys
import shutil
import json
import re
import urllib.parse
import subprocess

# --- Configuración de Rutas ---
WORKSPACE_DIR = "/Users/makebyjordan/local/myweb2teach"
SOURCE_CREACIONES = os.path.join(WORKSPACE_DIR, "allVideosPhotoIaALL/creaciones")
SOURCE_MARCAS = os.path.join(WORKSPACE_DIR, "allVideosPhotoIaALL/marcas")
WEB_ASSETS_CREACIONES = os.path.join(WORKSPACE_DIR, "web/assets/creaciones")
PROJECTS_JSON_PATH = os.path.join(WORKSPACE_DIR, "web/projects.json")
PROJECTS_HTML_DIR = os.path.join(WORKSPACE_DIR, "web/projects")

# Template HTML para las páginas de detalle
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Desglose de Anuncio IA</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="../style.css?v=2.0">
    
    <!-- Custom Page Styles -->
    <style>
        .back-nav {
            margin-top: calc(var(--header-height) + 20px);
            margin-bottom: 20px;
        }
        .project-meta-box {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-lg);
            padding: 30px;
            margin-bottom: 30px;
        }
        .md-viewer {
            background-color: #0b0b0e;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            padding: 24px;
            max-height: 450px;
            overflow-y: auto;
            margin-bottom: 30px;
        }
        .md-viewer h1, .md-viewer h2, .md-viewer h3 {
            color: var(--accent-gold);
            margin-top: 20px;
            margin-bottom: 12px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            padding-bottom: 6px;
        }
        .md-viewer h1:first-child, .md-viewer h2:first-child {
            margin-top: 0;
        }
        .md-viewer p {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 12px;
        }
        .md-viewer ul, .md-viewer ol {
            margin-left: 20px;
            margin-bottom: 16px;
            color: var(--text-secondary);
            font-size: 0.95rem;
        }
        .md-viewer li {
            margin-bottom: 6px;
        }
        .md-viewer code {
            background-color: rgba(255, 255, 255, 0.05);
            color: #e4e4e7;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.85em;
        }
        .md-viewer pre {
            background-color: #050507;
            border: 1px solid rgba(255,255,255,0.05);
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            margin-bottom: 16px;
        }
        .md-viewer pre code {
            background: none;
            padding: 0;
            font-size: 0.85rem;
            display: block;
        }
        .md-tag-badge {
            display: inline-block;
            background-color: rgba(255,255,255,0.05);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
            padding: 4px 10px;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 4px;
            margin-bottom: 10px;
        }
    </style>
    
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>

    <!-- Header Navigation -->
    <header class="main-header">
        <div class="header-container">
            <a href="../index.html" class="brand-logo">
                <span class="logo-dot crimson"></span>
                <span class="logo-dot gold"></span>
                Jordan<span class="tech-glow">AI_Ads</span>
            </a>
            <nav class="nav-links">
                <a href="../index.html">Showroom Principal</a>
                <a href="../index.html#metodologia">Metodología</a>
                <a href="../index.html#formacion">Formación</a>
            </nav>
            <div class="header-cta">
                <a href="../index.html" class="btn btn-outline btn-sm">Volver al Showroom</a>
            </div>
        </div>
    </header>

    <main class="container">
        
        <!-- Back Navigation Link -->
        <div class="back-nav">
            <a href="../index.html" class="btn btn-secondary btn-sm">
                <i class="fa-solid fa-arrow-left"></i> Volver al Showroom
            </a>
        </div>

        <div class="project-detail-layout vertical-layout">
            
            <!-- Left Column: Media Players & Original Markdown Documents -->
            <div class="media-column">
                
                <!-- Video Player -->
                <div class="project-meta-box">
                    <h3 class="showcase-title"><i class="fa-solid fa-circle-play"></i> Anuncio Vídeo Final Acabado</h3>
                    <div class="phone-mockup">
                        <div class="phone-notch"></div>
                        <video src="{video_url}" controls autoplay loop muted playsinline></video>
                    </div>
                </div>

                <!-- Reference Image Slider -->
                {image_slider_block}

                <!-- Markdown Files Showcased -->
                {markdown_files_block}
            </div>

            <!-- Right Column: Prompts, CapCut instructions, & Custom Training -->
            <div class="details-column">
                <div class="project-meta-box">
                    <span class="card-brand">{brand}</span>
                    <h2 class="card-title" style="font-size: 1.8rem; margin-bottom: 14px;">Showroom y Metodología</h2>
                    <p style="color: var(--text-secondary); margin-bottom: 20px;">
                        {description}
                    </p>
                </div>

                <!-- Prompts List -->
                <div class="project-meta-box">
                    <h3 class="showcase-title"><i class="fa-solid fa-code"></i> Fórmulas de Prompts Utilizadas</h3>
                    {prompts_list_block}
                </div>

                <!-- CapCut Guide -->
                {capcut_guide_block}

                <!-- Educational Section -->
                <div class="project-meta-box">
                    <h4 class="detail-training-title"><i class="fa-solid fa-graduation-cap"></i> Lecciones de este Proyecto</h4>
                    <div class="detail-training-body">
                        <p>Este proyecto representa la técnica de **consistencia visual** guiada por referencias cruzadas.</p>
                        <ul>
                            <li><strong>Coherencia de Estructura:</strong> Se preservan los elementos tridimensionales fijos de fondo usando guías de imagen en Google Flow.</li>
                            <li><strong>Postproducción:</strong> El vídeo se renderiza limpio y el texto publicitario y la música se montan externamente en CapCut.</li>
                        </ul>
                    </div>
                </div>

            </div>

        </div>
    </main>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container footer-bottom">
            <p>&copy; 2026 Jordan AI Ads. Diseñado con fines de entrenamiento y showcase de prompts.</p>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        // Interactive Image Slider
        const tabs = document.querySelectorAll('.selector-tab');
        const activeImg = document.getElementById('detail-active-img');

        if (tabs && activeImg) {
            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    tabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');
                    activeImg.src = tab.getAttribute('data-img-src');
                });
            });
        }

        // Copy to clipboard actions
        const copyBtns = document.querySelectorAll('.js-copy-prompt');
        copyBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const text = decodeURIComponent(btn.getAttribute('data-text'));
                navigator.clipboard.writeText(text).then(() => {
                    const originalText = btn.innerHTML;
                    btn.innerHTML = `<i class="fa-solid fa-circle-check"></i> ¡Copiado!`;
                    btn.style.color = '#10b981';
                    setTimeout(() => {
                        btn.innerHTML = originalText;
                        btn.style.color = '';
                    }, 2000);
                });
            });
        });
    </script>
</body>
</html>
"""

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')

def simple_markdown_to_html(md_text):
    # Escape HTML
    html = md_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Pre blocks
    code_blocks = []
    def save_code(match):
        code_blocks.append(match.group(1))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    html = re.sub(r'```(?:[a-zA-Z]*)\n([\s\S]*?)```', save_code, html)
    
    # Headers
    html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html, flags=re.M)
    
    # Lists
    html = re.sub(r'^\s*[-*+]\s+(.*$)', r'<li>\1</li>', html, flags=re.M)
    
    # Inline styles
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Paragraphs (line by line simple wrapping)
    lines = html.split('\n')
    in_list = False
    result = []
    for line in lines:
        trimmed = line.strip()
        if not trimmed:
            if in_list:
                result.append("</ul>")
                in_list = False
            continue
            
        if trimmed.startswith("<li>"):
            if not in_list:
                result.append("<ul>")
                in_list = True
            result.append(line)
        elif trimmed.startswith("<h") or trimmed.startswith("__CODE_BLOCK_"):
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(line)
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(f"<p>{line}</p>")
            
    if in_list:
        result.append("</ul>")
        
    html = "\n".join(result)
    
    # Restore code blocks
    for idx, code in enumerate(code_blocks):
        html = html.replace(f"__CODE_BLOCK_{idx}__", f"<pre><code>{code.strip()}</code></pre>")
        
    return html

def parse_prompts_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find prompts using regex
    # Match headers and code blocks
    pattern = r'(###\s+.*?(?:\n|$))(.*?)(```[\s\S]*?```)'
    matches = re.findall(pattern, content)
    
    prompts = []
    for title_line, desc_block, code_block in matches:
        title = title_line.replace('###', '').strip()
        code = code_block.replace('```', '').strip()
        # Clean any programming language name
        code_lines = code.split('\n')
        if code_lines and len(code_lines[0]) < 10 and not code_lines[0].startswith(' '):
            code = '\n'.join(code_lines[1:])
            
        # Extract brief conseil or description
        tip = "Mantén la coherencia visual."
        if "Consejo" in desc_block or "tip" in desc_block.lower():
            lines = desc_block.split('\n')
            for l in lines:
                if "Consejo:" in l or "Tip:" in l:
                    tip = l.split(':', 1)[1].strip()
                    break
        
        prompts.append({
            "title": title,
            "code": code,
            "tip": tip
        })
        
    return prompts

def analyze_and_update():
    print("=== [ANALIZA] Iniciando escaneo de nuevos anuncios ===")
    
    # Cargar base de datos actual
    if os.path.exists(PROJECTS_JSON_PATH):
        with open(PROJECTS_JSON_PATH, 'r', encoding='utf-8') as f:
            projects = json.load(f)
    else:
        projects = []
        
    registered_videos = {p['videoUrl'] for p in projects}
    new_projects_detected = []
    
    # Escanear creaciones
    for root, dirs, files in os.walk(SOURCE_CREACIONES):
        for file in files:
            if file.endswith('.mp4'):
                video_full_path = os.path.join(root, file)
                # Ruta relativa a SOURCE_CREACIONES
                rel_path = os.path.relpath(video_full_path, SOURCE_CREACIONES)
                local_web_url = f"./assets/creaciones/{urllib.parse.quote(rel_path)}"
                
                if local_web_url in registered_videos:
                    continue
                    
                print(f"\n[!] ¡Nuevo vídeo detectado!: {rel_path}")
                
                # Encontrar el directorio de la campaña
                # Si el video está en un subdirectorio "video" o "videos", subimos un nivel
                parent_dir = os.path.dirname(video_full_path)
                campaign_dir = parent_dir
                if os.path.basename(parent_dir) in ["video", "videos"]:
                    campaign_dir = os.path.dirname(parent_dir)
                    
                # Marca a la que pertenece (el primer subdirectorio de creaciones)
                brand_rel = os.path.relpath(campaign_dir, SOURCE_CREACIONES)
                brand_parts = brand_rel.split(os.sep)
                brand_slug = brand_parts[0] if brand_parts else "general"
                
                brand_name = brand_slug.capitalize()
                if brand_slug == "reforma-tipo-1":
                    brand_name = "Reforma Tipo 1"
                elif brand_slug == "inteligencia-sevilla":
                    brand_name = "Inteligencia Sevilla"
                
                campaign_name = os.path.basename(campaign_dir)
                campaign_title = f"{brand_name} — {campaign_name.replace('-', ' ').replace('_', ' ').title()}"
                
                # Slug para la página de detalle
                slug = slugify(campaign_name)
                # Evitar colisión de slug
                temp_slug = slug
                counter = 1
                while os.path.exists(os.path.join(PROJECTS_HTML_DIR, f"{temp_slug}.html")):
                    temp_slug = f"{slug}-{counter}"
                    counter += 1
                slug = temp_slug
                
                # Buscar imágenes en el directorio de la campaña
                campaign_images = []
                for img_root, img_dirs, img_files in os.walk(campaign_dir):
                    for img_file in img_files:
                        if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                            # Ruta completa de la imagen en all/
                            img_full_path = os.path.join(img_root, img_file)
                            img_rel = os.path.relpath(img_full_path, SOURCE_CREACIONES)
                            campaign_images.append(img_rel)
                
                # Buscar archivo de prompts
                prompts_file = None
                markdown_files = []
                for f_root, f_dirs, f_files in os.walk(campaign_dir):
                    for f_file in f_files:
                        if f_file.endswith('.md'):
                            md_full = os.path.join(f_root, f_file)
                            markdown_files.append(md_full)
                            if "prompt" in f_file.lower():
                                prompts_file = md_full
                
                # Copiar directorio completo de campaña a la web
                dest_campaign_dir = os.path.join(WEB_ASSETS_CREACIONES, os.path.relpath(campaign_dir, SOURCE_CREACIONES))
                print(f" -> Copiando assets a {os.path.relpath(dest_campaign_dir, WORKSPACE_DIR)}...")
                if os.path.exists(dest_campaign_dir):
                    shutil.rmtree(dest_campaign_dir)
                shutil.copytree(campaign_dir, dest_campaign_dir)
                
                # Si hay marca.md en marcas/, copiarla también
                brand_md_src = os.path.join(SOURCE_MARCAS, brand_slug, "marca.md")
                brand_md_dest = os.path.join(WORKSPACE_DIR, "web/assets/marcas", brand_slug, "marca.md")
                if os.path.exists(brand_md_src):
                    os.makedirs(os.path.dirname(brand_md_dest), exist_ok=True)
                    shutil.copy(brand_md_src, brand_md_dest)
                    markdown_files.append(brand_md_src)
                
                # Definir mini-datos del proyecto
                proj_desc = "Campaña publicitaria generada con Inteligencia Artificial utilizando la técnica 3+1 y consistencia visual."
                if markdown_files:
                    # Leer primeras líneas del primer md
                    try:
                        with open(markdown_files[0], 'r', encoding='utf-8') as f:
                            first_lines = [f.readline().strip() for _ in range(5)]
                        filtered_lines = [l for l in first_lines if l and not l.startswith('#') and not l.startswith('-')]
                        if filtered_lines:
                            proj_desc = " ".join(filtered_lines)[:180] + "..."
                    except:
                        pass
                
                # Determinar miniatura (primera imagen del slider)
                thumbnail = "https://placehold.co/600x340/121217/f4f4f7?text=Anuncio+IA"
                if campaign_images:
                    thumbnail = f"./assets/creaciones/{urllib.parse.quote(campaign_images[0])}"
                
                # Generar HTML de detalle
                print(f" -> Generando página web/projects/{slug}.html...")
                
                # 1. Slider de fotos
                image_slider_block = ""
                if campaign_images:
                    selector_tabs = ""
                    for idx, img_rel in enumerate(campaign_images[:3]):
                        active_class = " active" if idx == 0 else ""
                        tab_name = f"{idx+1}. Imagen"
                        if idx == 0: tab_name = "1. Antes"
                        elif idx == 1: tab_name = "2. Obra"
                        elif idx == 2: tab_name = "3. Después"
                        
                        img_web_path = f"../assets/creaciones/{urllib.parse.quote(img_rel)}"
                        selector_tabs += f'<button class="selector-tab{active_class}" data-img-src="{img_web_path}">{tab_name}</button>\n'
                        
                    first_img_web_path = f"../assets/creaciones/{urllib.parse.quote(campaign_images[0])}"
                    image_slider_block = f"""
                <div class="project-meta-box">
                    <h3 class="showcase-title"><i class="fa-regular fa-image"></i> Fotogramas Clave de Referencia (Prompts Ancla)</h3>
                    <div class="showcase-selector">
                        {selector_tabs}
                    </div>
                    <div class="phone-mockup">
                        <div class="phone-notch"></div>
                        <img id="detail-active-img" src="{first_img_web_path}" alt="Fotograma clave">
                    </div>
                </div>"""
                
                # 2. Markdown viewers
                markdown_files_block = ""
                for md_path in markdown_files[:2]:
                    md_rel_workspace = os.path.relpath(md_path, os.path.join(SOURCE_CREACIONES, ".."))
                    md_filename = os.path.basename(md_path)
                    try:
                        with open(md_path, 'r', encoding='utf-8') as f:
                            md_content = f.read()
                        html_content = simple_markdown_to_html(md_content)
                        markdown_files_block += f"""
                <div class="project-meta-box">
                    <span class="md-tag-badge">Fichero de Apoyo Duplicado</span>
                    <h3 class="showcase-title"><i class="fa-regular fa-file-lines"></i> {md_rel_workspace}</h3>
                    <div class="md-viewer">
                        {html_content}
                    </div>
                </div>"""
                    except Exception as e:
                        print(f"Error parsing md {md_filename}: {e}")
                
                # 3. Prompts list
                prompts_list_block = ""
                parsed_prompts = []
                if prompts_file:
                    parsed_prompts = parse_prompts_file(prompts_file)
                
                if parsed_prompts:
                    for idx, p in enumerate(parsed_prompts):
                        safe_code = urllib.parse.quote(p['code'])
                        prompts_list_block += f"""
                    <div class="prompt-panel">
                        <div class="prompt-panel-header">
                            <span class="prompt-panel-title">{p['title']}</span>
                            <button class="copy-btn js-copy-prompt" data-text="{safe_code}">
                                <i class="fa-regular fa-copy"></i> Copiar Prompt
                            </button>
                        </div>
                        <div class="prompt-content">
                            <pre><code>{p['code']}</code></pre>
                        </div>
                        <div class="prompt-tip">
                            <strong>Consejo:</strong> {p['tip']}
                        </div>
                    </div>"""
                else:
                    prompts_list_block = f"""
                    <div class="prompt-panel">
                        <div class="prompt-content">
                            <p style="color: var(--text-muted);">No se encontraron prompts estructurados en código. Lee los ficheros Markdown adjuntos para estudiar la campaña.</p>
                        </div>
                    </div>"""
                    
                # 4. CapCut Guide
                capcut_guide_block = ""
                if prompts_file:
                    try:
                        with open(prompts_file, 'r', encoding='utf-8') as f:
                            text = f.read()
                        capcut_section = re.search(r'(?:CapCut|Montaje|Instrucciones de Montaje)([\s\S]*?)(?:Lecciones|Lección|$)', text)
                        if capcut_section:
                            guide_text = capcut_section.group(1).strip()
                            guide_html = simple_markdown_to_html(guide_text)
                            capcut_guide_block = f"""
                <div class="project-meta-box">
                    <h3 class="showcase-title"><i class="fa-solid fa-scissors"></i> Instrucciones de Montaje en CapCut</h3>
                    <div class="prompt-panel">
                        <div class="prompt-content" style="max-height: none;">
                            {guide_html}
                        </div>
                    </div>
                </div>"""
                    except:
                        pass
                
                # Escribir el HTML
                project_html = HTML_TEMPLATE
                project_html = project_html.replace("{title}", campaign_name.replace('-', ' ').title())
                project_html = project_html.replace("{video_url}", f"../assets/creaciones/{urllib.parse.quote(rel_path)}")
                project_html = project_html.replace("{image_slider_block}", image_slider_block)
                project_html = project_html.replace("{markdown_files_block}", markdown_files_block)
                project_html = project_html.replace("{brand}", brand_name)
                project_html = project_html.replace("{description}", proj_desc)
                project_html = project_html.replace("{prompts_list_block}", prompts_list_block)
                project_html = project_html.replace("{capcut_guide_block}", capcut_guide_block)
                
                with open(os.path.join(PROJECTS_HTML_DIR, f"{slug}.html"), 'w', encoding='utf-8') as f:
                    f.write(project_html)
                
                # Crear nuevo objeto JSON
                new_project = {
                    "id": len(projects) + 1,
                    "title": campaign_title,
                    "brand": brand_name,
                    "brandSlug": brand_slug,
                    "projectPage": f"{slug}.html",
                    "type": "Antes / Obra / Final (Flujo 3+1)" if len(campaign_images) >= 3 else "UGC / Anuncio IA",
                    "desc": proj_desc,
                    "thumbnail": thumbnail,
                    "videoUrl": local_web_url
                }
                
                projects.append(new_project)
                new_projects_detected.append(campaign_title)
                
    if not new_projects_detected:
        print("\n[v] No se han detectado nuevos anuncios. Todo el contenido está actualizado.")
        return False
        
    # Guardar base de datos actualizada
    print(f"\n[+] Guardando base de datos con {len(new_projects_detected)} nuevos proyectos...")
    with open(PROJECTS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=2, ensure_ascii=False)
        
    # --- Ejecutar Despliegue (rsync) ---
    print("\n[+] Desplegando cambios al servidor Hestia (Cloudflare: jordanstarter.eu)...")
    try:
        subprocess.run([
            "rsync", "-avz", 
            os.path.join(WORKSPACE_DIR, "web/"), 
            "hestia-is:web/jordanstarter.eu/public_html/"
        ], check=True)
        print(" -> Despliegue completado con éxito.")
    except Exception as e:
        print(f" -> ERROR en despliegue: {e}")
        
    # --- Git Commit y Git Push ---
    print("\n[+] Vinculando y subiendo los cambios a GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True, cwd=WORKSPACE_DIR)
        commit_msg = f"feat: add {', '.join(new_projects_detected)} from automated allVideosPhotoIaALL analysis"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, cwd=WORKSPACE_DIR)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True, cwd=WORKSPACE_DIR)
        print(" -> Cambios subidos a GitHub con éxito.")
    except Exception as e:
        print(f" -> ERROR en Git push: {e}")
        
    print(f"\n=== [ANALIZA] Proceso finalizado. Se han añadido {len(new_projects_detected)} proyectos. ===")
    return True

if __name__ == "__main__":
    analyze_and_update()
