import streamlit as st

# --- Seiten-Konfiguration ---
st.set_page_config(
    page_title="Frage",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Bild URLs ---
IMG_JUMPHOUSE = "https://www.hamburg.de/resource/image/406012/landscape_ratio16x9/1240/697/13da6ae95443c66842a892d481476ca/867C02CEFA3C808D4962846D57A0774C/gallery-1-neuesstartbild.jpg"
IMG_WUNDERLAND = "https://www.miniatur-wunderland.de/assets/content/layout/italien/italien-riomaggiore-highangle.jpg"

# --- State Management ---
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'choice' not in st.session_state:
    st.session_state.choice = ""

# --- Globales CSS (Gilt für alle Seiten) ---
st.markdown("""
    <style>
    /* Reset: Ränder entfernen */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100%;
    }
    header, footer {display: none !important;}
    
    /* Button Design (Clean & Modern) */
    div.stButton > button {
        background-color: white; 
        color: black;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        color: #333;
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SEITE 1: Intro mit animiertem Hintergrund
# ==========================================
if st.session_state.page == 1:
    
    # CSS speziell für Seite 1 (Animierter Gradient)
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Titel Styling Seite 1 */
    .title-text {
        text-align: center;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        font-size: 40px;
        margin-top: 35vh; /* Schiebt Text in die Mitte */
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Inhalt
    st.markdown('<div class="title-text">Ich habe eine Frage an dich</div>', unsafe_allow_html=True)
    
    # Button Zentrierung
    col1, col2, col3 = st.columns([1, 0.5, 1]) # Mittlere Spalte schmaler -> Button kleiner
    with col2:
        if st.button("Zur Frage"):
            st.session_state.page = 2
            st.rerun()

# ==========================================
# SEITE 2: Split Screen (Perfekt zentriert)
# ==========================================
elif st.session_state.page == 2:
    
    # CSS für Split Screen Hintergründe
    st.markdown(f"""
    <style>
    /* Linkes Bild */
    .bg-left {{
        position: fixed;
        top: 0; left: 0;
        width: 50vw; height: 100vh;
        background-image: url("{IMG_JUMPHOUSE}");
        background-size: cover; background-position: center;
        z-index: 0;
    }}
    /* Rechtes Bild */
    .bg-right {{
        position: fixed;
        top: 0; right: 0;
        width: 50vw; height: 100vh;
        background-image: url("{IMG_WUNDERLAND}");
        background-size: cover; background-position: center;
        z-index: 0;
    }}
    /* Titel oben */
    .top-title {{
        position: fixed;
        top: 50px;
        width: 100%;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 0 2px 10px rgba(0,0,0,0.7);
        z-index: 2;
        font-family: sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Hintergründe rendern
    st.markdown('<div class="bg-left"></div>', unsafe_allow_html=True)
    st.markdown('<div class="bg-right"></div>', unsafe_allow_html=True)
    st.markdown('<div class="top-title">Wo möchtest du mit mir hingehen?</div>', unsafe_allow_html=True)

    # --- Layout Trick für vertikale Zentrierung ---
    
    # 1. Wir schieben alles nach unten (ca. 45% der Bildschirmhöhe)
    st.markdown('<div style="height: 45vh;"></div>', unsafe_allow_html=True)
    
    # 2. Zwei Spalten für die Knöpfe
    c1, c2 = st.columns(2)
    
    # LINKS (Jumphouse)
    with c1:
        # Nested Columns für horizontale Zentrierung
        # [1, 2, 1] bedeutet: Platzhalter, Button (doppelt so breit), Platzhalter
        lc1, lc2, lc3 = st.columns([1, 2, 1])
        with lc2:
            if st.button("Zum Jumphouse"):
                st.session_state.choice = "Jumphouse"
                st.session_state.page = 3
                st.rerun()

    # RECHTS (Wunderland)
    with c2:
        rc1, rc2, rc3 = st.columns([1, 2, 1])
        with rc2:
            if st.button("Zum Miniaturwunderland"):
                st.session_state.choice = "Wunderland"
                st.session_state.page = 3
                st.rerun()

# ==========================================
# SEITE 3: Ergebnis
# ==========================================
elif st.session_state.page == 3:
    st.markdown("""
    <style>
    .stApp {
        background-color: #111;
        color: white;
        text-align: center;
    }
    h1 { margin-top: 40vh; font-family: sans-serif; }
    p { font-size: 20px; color: #ccc; }
    </style>
    """, unsafe_allow_html=True)
    
    if st.session_state.choice == "Jumphouse":
        st.title("Jumphouse.")
        st.write("Gute Wahl. Wir gehen springen.")
    else:
        st.title("Miniaturwunderland.")
        st.write("Cool. Wir schauen uns die Züge an.")