import streamlit as st

# --- Konfiguration: WICHTIG! Layout auf "wide" setzen ---
st.set_page_config(
    page_title="Frage...",
    page_icon="😏",
    layout="wide",  # Nutzt die volle Breite
    initial_sidebar_state="collapsed"
)

# --- URLs der Bilder ---
IMG_JUMPHOUSE = "https://www.hamburg.de/resource/image/406012/landscape_ratio16x9/1240/697/13da6ae95443c66842a892d481476ca/867C02CEFA3C808D4962846D57A0774C/gallery-1-neuesstartbild.jpg"
IMG_WUNDERLAND = "https://www.miniatur-wunderland.de/assets/content/layout/italien/italien-riomaggiore-highangle.jpg"

# --- State Management ---
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'choice' not in st.session_state:
    st.session_state.choice = ""

# --- Globales CSS für Layout & Vibe ---
st.markdown(f"""
    <style>
    /* 1. Alles auf 0 setzen für Fullscreen-Look */
    .block-container {{
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }}
    
    /* Header ausblenden */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Style für die Überschriften */
    h1 {{
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        color: white;
        text-shadow: 2px 2px 8px #000000;
        z-index: 999;
        position: relative;
    }}

    /* Button Styling - Modern & Clean */
    div.stButton > button {{
        display: block;
        margin: 0 auto;
        background-color: rgba(255, 255, 255, 0.9);
        color: #000;
        border: none;
        border-radius: 8px;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 20px;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }}
    div.stButton > button:hover {{
        background-color: #fff;
        transform: scale(1.05);
        color: #ff4b4b;
    }}
    
    /* --- Split Screen Logik für Seite 2 --- */
    
    /* Linke Spalte (Jumphouse) Hintergrund */
    div[data-testid="column"]:nth-of-type(1) {{
        background-image: url("{IMG_JUMPHOUSE}");
        background-size: cover;
        background-position: center;
        height: 100vh; /* Volle Höhe */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Vertikal mittig */
        align-items: center;
    }}
    
    /* Rechte Spalte (Wunderland) Hintergrund */
    div[data-testid="column"]:nth-of-type(2) {{
        background-image: url("{IMG_WUNDERLAND}");
        background-size: cover;
        background-position: center;
        height: 100vh; /* Volle Höhe */
        display: flex;
        flex-direction: column;
        justify-content: center; /* Vertikal mittig */
        align-items: center;
    }}
    
    /* Overlay Title auf Seite 2 */
    .floating-title {{
        position: absolute;
        top: 5vh;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-shadow: 0px 0px 10px rgba(0,0,0,0.8);
        z-index: 100;
        pointer-events: none; /* Klicks gehen durch */
    }}
    
    </style>
    """, unsafe_allow_html=True)

# --- SEITE 1: Intro (Lockerer Vibe) ---
if st.session_state.page == 1:
    # Hintergrund für Seite 1 (Dunkel/Modern)
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e1e 0%, #3a3a3a 100%);
    }
    </style>
    """, unsafe_allow_html=True)

    # Vertikale Zentrierung simulieren
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.title("Ich hab da mal ne Frage... 😏")
    
    st.write("")
    st.write("")
    
    # Button mittig
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.write("")
        st.write("")
        if st.button("Schieß los"):
            st.session_state.page = 2
            st.rerun()

# --- SEITE 2: Der Split Screen ---
elif st.session_state.page == 2:
    
    # Der Titel schwebt über allem
    st.markdown('<div class="floating-title">Wo geht\'s hin?</div>', unsafe_allow_html=True)

    # Das Layout: Zwei Spalten, kein Abstand (gap=0)
    c1, c2 = st.columns(2, gap="small") 
    # Hinweis: gap="small" ist technisch nötig, das CSS überschreibt den visuellen Abstand

    with c1:
        # Hier ist nichts drin außer Abstandhaltern, weil das CSS das Bild setzt
        # Wir brauchen nur den Button
        # Wir nutzen Container um den Button etwas nach unten zu schieben falls nötig
        st.write("") 
        st.write("") 
        if st.button("Jumphouse 🤸‍♂️"):
            st.session_state.choice = "Jumphouse"
            st.session_state.page = 3
            st.rerun()

    with c2:
        st.write("") 
        st.write("") 
        if st.button("Miniatur Wunderland 🚂"):
            st.session_state.choice = "Wunderland"
            st.session_state.page = 3
            st.rerun()

# --- SEITE 3: Ergebnis ---
elif st.session_state.page == 3:
    st.markdown("""
    <style>
    .stApp {
        background: #111;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.balloons()
    
    st.write("")
    st.write("")
    st.write("")
    
    st.title("Alles klar. 😉")
    
    if st.session_state.choice == "Jumphouse":
        st.markdown("<h3 style='text-align: center;'>Dann pack die Sportsachen ein. Wir gehen springen.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center;'>Gute Wahl. Bisschen Kultur und staunen.</h3>", unsafe_allow_html=True)
        
    st.write("")
    st.markdown("<p style='text-align: center; color: #888;'>Ich schreib dir wann/wo.</p>", unsafe_allow_html=True)