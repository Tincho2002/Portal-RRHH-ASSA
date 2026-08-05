import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Portal de RRHH",
    page_icon="https://cdn.jsdelivr.net/gh/Tincho2002/RRHH@main/assets/logo_assa.jpg",
    layout="wide"
)

# ----------------------------------------------------------------------------------
# --- CSS: PANTALLA DE CARGA, ANIMACIONES Y TARJETAS COMPACTAS DARK ---
# ----------------------------------------------------------------------------------
st.markdown("""
<style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&display=swap');

    /* Ocultar por completo la barra lateral nativa de Streamlit */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* Pantalla de Carga (Splash Screen) con fondo oscuro/corporativo */
    #splash-screen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #0d1117, #161b22, #1f242d);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-family: 'Source Sans Pro', sans-serif;
        
        animation: slideUpSplash 1s ease-out 2.5s forwards;
    }

    #splash-logo {
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.2);
        border: 2px solid rgba(0, 212, 255, 0.3);
        animation: fadeInScale 1.5s 0.5s ease-out forwards;
    }

    #splash-title {
        margin-top: 20px;
        color: #00d4ff;
        font-weight: 700;
        letter-spacing: 1px;
        animation: fadeInSlide 1.5s 1s ease-out forwards;
    }

    /* Keyframes Animaciones */
    @keyframes slideUpSplash {
        from { transform: translateY(0); }
        to { transform: translateY(-100vh); visibility: hidden; }
    }

    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes fadeInSlide {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Animación de Gotas de Agua / Estilo Looker */
    .droplet {
        position: absolute;
        bottom: 100%;
        width: 2px;
        height: 50px;
        background: linear-gradient(to top, rgba(0, 212, 255, 0.8), rgba(0, 212, 255, 0.1));
        border-radius: 50%;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(100vh); } }

    /* --- Fondo Global Oscuro (Look Looker Studio) --- */
    .stApp {
        background-color: #0e1117 !important;
        color: #e2e8f0;
    }

    /* --- Animación del Contenido Principal --- */
    #main-content {
        opacity: 0; 
        animation: showContent 1.5s ease-in 2.5s forwards;
    }
    @keyframes showContent {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* =========================================
       2. TARJETAS MÁS PEQUEÑAS Y COMPACTAS
       ========================================= */
    
    .cards-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
        perspective: 1000px;
        padding: 10px 0;
        font-family: 'Source Sans Pro', sans-serif;
    }

    /* Tarjeta Dark más compacta */
    .nav-card {
        background: #161b22;
        border-radius: 12px;
        padding: 20px 18px;
        width: 230px; 
        text-decoration: none !important;
        color: #f8fafc !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid #30363d;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        flex-grow: 0; 
        max-width: 260px;
        cursor: pointer;
    }

    /* Efecto Hover Luminoso tipo Panel Looker */
    .nav-card:hover {
        transform: translateY(-6px) scale(1.02);
        background: #1c2128;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
        border-color: #00d4ff;
    }

    /* Estilos de bordes superiores distintivos por tarjeta */
    .card-cyan { border-top: 4px solid #00d4ff; }
    .card-indigo { border-top: 4px solid #6366f1; }
    .card-violet { border-top: 4px solid #a855f7; }
    .card-slate { border-top: 4px solid #64748b; }
    .card-blue { border-top: 4px solid #3b82f6; }
    .card-orange { border-top: 4px solid #f97316; }

    /* Iconos más chicos y estilizados */
    .card-icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
        transition: transform 0.4s ease;
        padding: 8px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.03);
        width: 55px;
        height: 55px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .card-cyan .card-icon { color: #00d4ff; box-shadow: 0 0 12px rgba(0,212,255,0.1); }
    .card-indigo .card-icon { color: #6366f1; box-shadow: 0 0 12px rgba(99,102,241,0.1); }
    .card-violet .card-icon { color: #a855f7; box-shadow: 0 0 12px rgba(168,85,247,0.1); }
    .card-slate .card-icon { color: #94a3b8; box-shadow: 0 0 12px rgba(148,163,184,0.1); }
    .card-blue .card-icon { color: #3b82f6; box-shadow: 0 0 12px rgba(59,130,246,0.1); }
    .card-orange .card-icon { color: #f97316; box-shadow: 0 0 12px rgba(249,115,22,0.1); }

    .nav-card:hover .card-icon {
        transform: scale(1.1) rotate(5deg);
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 8px;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    .card-desc {
        font-size: 0.83rem;
        color: #94a3b8;
        margin-bottom: 15px;
        line-height: 1.35;
        flex-grow: 1; 
    }

    /* Botón de acceso circular compacto */
    .go-btn {
        background-color: #21262d;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 3px 8px rgba(0,0,0,0.3);
        font-size: 0.95rem;
        color: #8b949e;
        transition: all 0.3s ease;
        align-self: center;
        margin-top: auto;
        border: 1px solid #30363d;
    }
    
    .nav-card:hover .go-btn {
        background-color: #00d4ff;
        color: #0d1117;
        box-shadow: 0 0 10px rgba(0,212,255,0.5);
        border-color: #00d4ff;
        transform: scale(1.1);
    }
    
    /* Header Responsive Alineado al Centro */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        padding: 10px 0;
    }
    .header-text { text-align: center; flex-grow: 1; }
    .header-logo { width: 170px; flex-shrink: 0; height: auto; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); border: 1px solid #30363d; align-self: center; }

    /* Estilo para la píldora de versión / estado */
    .status-badge {
        display: inline-flex;
        align-items: center;
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        color: #8b949e;
        gap: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #00d4ff;
        border-radius: 50%;
        box-shadow: 0 0 8px #00d4ff;
    }

    @media (max-width: 768px) {
        .header-container { flex-direction: column; justify-content: center; }
        .header-logo { width: 140px; }
        .cards-grid { flex-direction: column; align-items: center; }
        .nav-card { width: 100%; max-width: 100%; }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------
# --- HTML: PANTALLA DE CARGA ---
# -----------------------------------------------------------------------
st.html("""
<div id="splash-screen">
    <script>
        const splash = document.getElementById('splash-screen');
        for (let i = 0; i < 40; i++) {
            const droplet = document.createElement('div');
            droplet.className = 'droplet';
            droplet.style.left = `${Math.random() * 100}vw`;
            droplet.style.animationDuration = `${0.6 + Math.random() * 0.4}s`;
            droplet.style.animationDelay = `${Math.random() * 3}s`;
            splash.appendChild(droplet);
        }
    </script>
    <img id="splash-logo" src="https://cdn.jsdelivr.net/gh/Tincho2002/RRHH@main/assets/logo_assa.jpg" width="400">
    <h1 id="splash-title">Portal de Análisis de RRHH - ASSA</h1>
</div>
""")

# -----------------------------------------------------------------------
# --- CONTENIDO PRINCIPAL ---
# -----------------------------------------------------------------------
st.markdown('<div id="main-content">', unsafe_allow_html=True)

# Header perfectamente alineado
logo_url = "https://cdn.jsdelivr.net/gh/Tincho2002/RRHH@main/assets/logo_assa.jpg"
st.markdown(f"""
<div class="header-container">
    <img src="{logo_url}" class="header-logo logo-left">
    <div class="header-text">
        <h1 style='color:#f8fafc; font-size: 2.1rem; margin:0; font-weight: 700;'>Bienvenido al Portal de RRHH</h1>
        <h3 style='color:#00d4ff; margin:6px 0; font-size: 1.1rem; font-weight: 600;'>Tableros de Control & Análisis Estratégico</h3>
        <h4 style='color:#94a3b8; margin:0; font-weight: 400; font-size: 0.95rem;'>Aguas Santafesinas S.A.</h4>
    </div>
    <img src="{logo_url}" class="header-logo logo-right">
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border-color: #30363d; margin: 25px 0;'>", unsafe_allow_html=True)

# Texto Intro
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 25px;">
        <h2 style="color: #f8fafc; font-size: 1.4rem; font-weight: 600;">Central Operativa de Capital Humano</h2>
        <p style="color: #94a3b8; font-size: 1rem;">Selecciona una de las tarjetas interactivas para acceder de forma directa a los reportes actualizados.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- TARJETAS COMPACTAS (ESTILO DARK LOOKER CON OPERARIO ANIMADO) ---
cards_html = """
<div class="cards-grid">
    <!-- Dotación -->
    <a href="https://datastudio.google.com/u/0/reporting/4dbaf434-c14f-404a-8dc1-3a8b60493e9b/page/p_q8rizdfu3d" target="_blank" class="nav-card card-cyan">
        <div class="card-icon">👥</div>
        <div class="card-title">Dotación</div>
        <div class="card-desc">Estructura y distribución geográfica y por gerencia.</div>
        <div class="go-btn">➜</div>
    </a>
    <!-- Horas Extras -->
    <a href="https://datastudio.google.com/u/0/reporting/e9f3e7b1-abc2-4340-9e9d-7ab34acdd37e/page/p_g4bdxiyn3d" target="_blank" class="nav-card card-indigo">
        <div class="card-icon">⏰</div>
        <div class="card-title">Horas Extras</div>
        <div class="card-desc">Seguimiento de horas adicionales al 50% y 100%.</div>
        <div class="go-btn">➜</div>
    </a>
    <!-- Masa Salarial -->
    <a href="https://datastudio.google.com/u/0/reporting/01d0ae36-7afd-4808-af5e-62ed86d6b6a8/page/p_9w1co7ys5d" target="_blank" class="nav-card card-violet">
        <div class="card-icon">💸</div>
        <div class="card-title">Masa Salarial</div>
        <div class="card-desc">Evolución y proyecciones de costos salariales.</div>
        <div class="go-btn">➜</div>
    </a>
    <!-- Planta de Cargos -->
    <a href="https://datastudio.google.com/u/0/reporting/1d6aef6a-60a4-431a-a3b4-d123326b08e9/page/p_q9g37hfx5d" target="_blank" class="nav-card card-slate">
        <div class="card-icon">📊</div>
        <div class="card-title">Planta de Cargos</div>
        <div class="card-desc">Dinámica de ingresos, egresos y composición.</div>
        <div class="go-btn">➜</div>
    </a>
    <!-- Ausentismo -->
    <a href="https://datastudio.google.com/u/0/reporting/5b7aa567-6e22-470d-82ed-037033e93d9d/page/p_g64w8hmi5d" target="_blank" class="nav-card card-blue">
        <div class="card-icon">📅</div>
        <div class="card-title">Ausentismo</div>
        <div class="card-desc">Control de indicadores clave de ausentismo.</div>
        <div class="go-btn">➜</div>
    </a>
    <!-- Guardias 3T con Operario Animado -->
    <a href="https://datastudio.google.com/u/0/reporting/3206a509-6a38-424b-bf14-48cea3df3e9e/page/p_i276woun3d" target="_blank" class="nav-card card-orange">
        <div class="card-icon">
            <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f477_1f3fc/512.gif" width="45" height="45" alt="👷">
        </div>
        <div class="card-title">Guardias 3T</div>
        <div class="card-desc">Comparativa de turnos rotativos y optimización.</div>
        <div class="go-btn">➜</div>
    </a>
</div>
"""

st.html(cards_html)

# --- PIé DE PÁGINA PROFESIONAL CON BADGE DE ESTADO ---
st.markdown("<hr style='border-color: #30363d; margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; padding-bottom: 20px;">
    <div class="status-badge">
        <div class="status-dot"></div>
        <span>Sistema Activo • Módulo RRHH ASSA</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Cierre main-content
