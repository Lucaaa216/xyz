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

# --- CSS Design (Minimalistisch & Bilder Fix) ---
st.markdown(f"""
    <style>
    /* Entfernt den weißen Standard-Rand von Streamlit oben/links/rechts */
    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100%;
    }}
    
    /* Header und Footer ausblenden */
    header, footer {{display: none !important;}}
    
    /* Button Design (Clean, Schwarz/Weiß) */
    div.stButton > button {{
        background-color: white;
        color: black;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: all 0.2s;
        width: 100%;
    }}
    div.stButton > button:hover {{
        background-color: #f0f0f0;
        border-color: #000;
    }}

    /* --- Hintergrund-Klassen für Seite 2 --- */
    .split-bg-left {{
        position: fixed;
        top: 0;
        left: 0;
        width: 50vw;
        height: 100vh;
        background-image: url("{IMG_JUMPHOUSE}");
        background-size: cover;
        background-position: center;
        z-index: 0;
    }}
    
    .split-bg-right {{
        position: fixed;
        top: 0;
        right: 0;
        width: 50vw; /* 50% der Viewport Width */
        height: 100vh;
        background-image: url("{IMG_WUNDERLAND}");
        background-size: cover;
        background-position: center;
        z-index: 0;
    }}
    
    /* Titel Style für Overlay */
    .overlay-title {{
        position: fixed;
        top: 10%;
        width: 100%;
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: bold;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.8);
        z-index: 2;
        font-family: sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SEITE 1: Intro
# ==========================================
if st.session_state.page == 1:
    # Dunkler Hintergrund für Seite 1
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
    }
    h1 { color: white; font-family: sans-serif; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    # Abstandshalter, um den Inhalt mittig zu bekommen
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.title("Ich habe eine Frage an dich")
    
    st.write("")
    st.write("")

    # Button zentriert
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Zur Frage"):
            st.session_state.page = 2
            st.rerun()

# ==========================================
# SEITE 2: Auswahl (Split Screen)
# ==========================================
elif st.session_state.page == 2:
    
    # 1. Wir rendern die Hintergründe manuell via HTML
    # Das umgeht das Problem, dass Streamlit-Spalten manchmal leer bleiben.
    st.markdown('<div class="split-bg-left"></div>', unsafe_allow_html=True)
    st.markdown('<div class="split-bg-right"></div>', unsafe_allow_html=True)
    
    # 2. Der Titel (schwebt darüber)
    st.markdown('<div class="overlay-title">Wo möchtest du mit mir hingehen?</div>', unsafe_allow_html=True)

    # 3. Die Buttons positionieren
    # Wir nutzen leere Container, um die Buttons nach unten zu schieben
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    # Layout Spalten für die Buttons
    c1, c2 = st.columns(2)

    with c1:
        # Linke Seite Button
        col_pad_l, col_btn_l, col_pad_r = st.columns([1, 2, 1])
        with col_btn_l:
            st.write("") # Kleiner Abstand
            if st.button("Zum Jumphouse"):
                st.session_state.choice = "Jumphouse"
                st.session_state.page = 3
                st.rerun()

    with c2:
        # Rechte Seite Button
        col_pad_l, col_btn_r, col_pad_r = st.columns([1, 2, 1])
        with col_btn_r:
            st.write("") # Kleiner Abstand
            if st.button("Zum Miniaturwunderland"):
                st.session_state.choice = "Wunderland"
                st.session_state.page = 3
                st.rerun()

# ==========================================
# SEITE 3: Ergebnis
# ==========================================
elif st.session_state.page == 3:
    # Einfacher weißer Text auf dunklem Grund
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    st.write("")
    
    if st.session_state.choice == "Jumphouse":
        st.header("Alles klar. Jumphouse.")
        st.write("Dann machen wir Sport.")
    else:
        st.header("Alles klar. Miniaturwunderland.")
        st.write("Dann schauen wir uns das an.")