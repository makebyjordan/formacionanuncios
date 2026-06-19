/* ==========================================================================
   Jordan AI Ads Studio — Lógica de Aplicación
   ========================================================================== */

let projects = [];

// --- Inicialización y Renderizado de Tarjetas ---
document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("projects.json");
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        projects = await response.json();
        renderProjects(projects);
        setupFilters();
        setupTrainingTabs();
    } catch (error) {
        console.error("Error loading projects database:", error);
        const grid = document.getElementById("projects-grid");
        if (grid) {
            grid.innerHTML = `<div class="no-projects">Error al cargar la base de datos de proyectos.</div>`;
        }
    }
});

// --- Renderizar Tarjetas en el Grid ---
function renderProjects(projectsList) {
    const grid = document.getElementById("projects-grid");
    grid.innerHTML = "";

    if (projectsList.length === 0) {
        grid.innerHTML = `<div class="no-projects">No se encontraron proyectos.</div>`;
        return;
    }

    projectsList.forEach(project => {
        const card = document.createElement("div");
        card.className = "project-card";
        card.setAttribute("data-brand", project.brandSlug);
        
        card.innerHTML = `
            <a href="projects/${project.projectPage}" class="card-media-link">
                <div class="card-media">
                    <img src="${project.thumbnail}" alt="${project.title}" onerror="this.src='https://placehold.co/600x340/121217/f4f4f7?text=Anuncio+IA'">
                    <span class="media-tag">${project.brand}</span>
                    <span class="media-play-icon"><i class="fa-solid fa-play"></i></span>
                </div>
            </a>
            <div class="card-content">
                <span class="card-brand">${project.brand}</span>
                <h3 class="card-title">${project.title}</h3>
                <p class="card-desc">${project.desc}</p>
                <div class="card-meta">
                    <span class="meta-type"><i class="fa-solid fa-wand-magic-sparkles"></i> ${project.type.split(" ")[0]}</span>
                    <a href="projects/${project.projectPage}" class="card-link">Ver Detalles <i class="fa-solid fa-arrow-right"></i></a>
                </div>
            </div>
        `;
        
        grid.appendChild(card);
    });
}

// --- Configuración de Filtros ---
function setupFilters() {
    const filterBtns = document.querySelectorAll(".filter-btn");
    
    filterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            // Activar botón
            filterBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            
            const filterValue = btn.getAttribute("data-filter");
            
            // Filtrar lógica
            if (filterValue === "all") {
                renderProjects(projects);
            } else {
                const filtered = projects.filter(p => p.brandSlug === filterValue);
                renderProjects(filtered);
            }
        });
    });
}

// --- Navegación de Tabs de Formación ---
function setupTrainingTabs() {
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");
    
    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            tabBtns.forEach(b => b.classList.remove("active"));
            tabContents.forEach(c => c.classList.remove("active"));
            
            btn.classList.add("active");
            const tabId = "tab-" + btn.getAttribute("data-tab");
            document.getElementById(tabId).classList.add("active");
        });
    });
}

// --- Lógica de Carga e Interacción de Skills de Claude ---
document.addEventListener("DOMContentLoaded", () => {
    setupSkillsViewer();
});

let currentRawSkillContent = "";

function setupSkillsViewer() {
    const skillBtns = document.querySelectorAll(".skill-item-btn");
    const viewerFilename = document.getElementById("viewer-filename");
    const viewerContent = document.getElementById("viewer-content-area");
    const copyBtn = document.getElementById("copy-skill-btn");
    
    if (skillBtns.length === 0) return;
    
    skillBtns.forEach(btn => {
        btn.addEventListener("click", async () => {
            // Activar botón en el menú
            skillBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            
            const skillName = btn.getAttribute("data-skill");
            viewerFilename.textContent = `${skillName}/SKILL.md`;
            
            // Mostrar estado de carga
            viewerContent.innerHTML = `
                <div class="viewer-placeholder">
                    <i class="fa-solid fa-circle-notch fa-spin"></i>
                    <h3>Cargando archivo...</h3>
                    <p>Obteniendo especificación técnica de la skill <code>${skillName}</code>...</p>
                </div>
            `;
            copyBtn.style.display = "none";
            
            try {
                const response = await fetch(`./skills/${skillName}/SKILL.md`);
                if (!response.ok) {
                    throw new Error(`Error HTTP: ${response.status}`);
                }
                const mdContent = await response.text();
                currentRawSkillContent = mdContent;
                
                // Renderizar
                viewerContent.innerHTML = renderMarkdown(mdContent);
                copyBtn.style.display = "inline-flex";
            } catch (error) {
                console.error("Error cargando skill:", error);
                viewerContent.innerHTML = `
                    <div class="viewer-placeholder">
                        <i class="fa-solid fa-circle-exclamation" style="color: #ff5f56;"></i>
                        <h3>Error de Carga</h3>
                        <p>No se pudo obtener el archivo <code>SKILL.md</code>. Asegúrate de que los archivos se copiaron correctamente.</p>
                    </div>
                `;
            }
        });
    });
    
    // Copiar al portapapeles
    if (copyBtn) {
        copyBtn.addEventListener("click", () => {
            if (!currentRawSkillContent) return;
            navigator.clipboard.writeText(currentRawSkillContent).then(() => {
                const originalHTML = copyBtn.innerHTML;
                copyBtn.innerHTML = `<i class="fa-solid fa-circle-check"></i> ¡Copiada!`;
                copyBtn.style.color = '#10b981';
                setTimeout(() => {
                    copyBtn.innerHTML = originalHTML;
                    copyBtn.style.color = '';
                }, 2000);
            });
        });
    }
}

// Visualizador Markdown custom
function renderMarkdown(md) {
    let blocks = md.split('\n\n');
    let resultHtml = [];
    
    for (let block of blocks) {
        let trimmed = block.trim();
        if (!trimmed) continue;
        
        // Code Block
        if (trimmed.startsWith('```')) {
            let code = trimmed.replace(/^```[a-zA-Z]*/, '').replace(/```$/, '');
            resultHtml.push(`<pre><code>${escapeHTML(code)}</code></pre>`);
            continue;
        }
        
        // Headers
        if (trimmed.startsWith('#')) {
            let level = 0;
            while (trimmed[level] === '#') level++;
            let text = trimmed.substring(level).trim();
            resultHtml.push(`<h${level}>${parseInline(text)}</h${level}>`);
            continue;
        }
        
        // Lists
        if (trimmed.startsWith('-') || trimmed.startsWith('*')) {
            let items = trimmed.split('\n');
            let listHtml = '<ul>';
            for (let item of items) {
                let text = item.replace(/^[-*]\s+/, '');
                listHtml += `<li>${parseInline(text)}</li>`;
            }
            listHtml += '</ul>';
            resultHtml.push(listHtml);
            continue;
        }
        
        // Paragraph / Plain Text
        let paragraphs = trimmed.split('\n');
        for (let p of paragraphs) {
            if (p.trim()) {
                resultHtml.push(`<p>${parseInline(p)}</p>`);
            }
        }
    }
    
    return resultHtml.join('\n');
}

function escapeHTML(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function parseInline(str) {
    let html = escapeHTML(str);
    // Bold
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    // Inline Code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
    return html;
}

