import streamlit as st
import time

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

# --- Globales CSS ---
st.markdown("""
    <style>
    /* Reset & Clean Up */
    .block-container { padding: 0 !important; margin: 0 !important; max-width: 100%; }
    header, footer { display: none !important; }
    
    /* Button Design */
    div.stButton > button {
        background-color: white; 
        color: black;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s, background-color 0.2s;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SEITE 1: Intro (Animierter Gradient)
# ==========================================
if st.session_state.page == 1:
    
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
    
    .title-text {
        text-align: center; color: white;
        font-family: sans-serif; font-weight: 300; font-size: 40px;
        margin-top: 35vh; margin-bottom: 30px;
        text-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title-text">Ich habe eine Frage an dich</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 0.6, 1])
    with c2:
        if st.button("Zur Frage"):
            st.session_state.page = 2
            st.rerun()

# ==========================================
# SEITE 2: Auswahl (Split Screen)
# ==========================================
elif st.session_state.page == 2:
    
    st.markdown(f"""
    <style>
    .bg-left {{
        position: fixed; top: 0; left: 0; width: 50vw; height: 100vh;
        background-image: url("{IMG_JUMPHOUSE}");
        background-size: cover; background-position: center; z-index: 0;
    }}
    .bg-right {{
        position: fixed; top: 0; right: 0; width: 50vw; height: 100vh;
        background-image: url("{IMG_WUNDERLAND}");
        background-size: cover; background-position: center; z-index: 0;
    }}
    .top-title {{
        position: fixed; top: 50px; width: 100%; text-align: center;
        color: white; font-size: 32px; font-weight: bold;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8); z-index: 2; font-family: sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="bg-left"></div>', unsafe_allow_html=True)
    st.markdown('<div class="bg-right"></div>', unsafe_allow_html=True)
    st.markdown('<div class="top-title">Wo möchtest du mit mir hingehen?</div>', unsafe_allow_html=True)

    # Platzhalter für Zentrierung
    st.markdown('<div style="height: 45vh;"></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    
    with c1: # LINKS
        lc1, lc2, lc3 = st.columns([1, 2, 1])
        with lc2:
            if st.button("Zum Jumphouse"):
                st.session_state.choice = "Jumphouse"
                st.balloons()          # Animation
                time.sleep(1.5)        # Kurze Pause damit man Animation sieht
                st.session_state.page = 3
                st.rerun()

    with c2: # RECHTS
        rc1, rc2, rc3 = st.columns([1, 2, 1])
        with rc2:
            if st.button("Zum Miniaturwunderland"):
                st.session_state.choice = "Wunderland"
                st.snow()              # Animation (Schnee passt gut zu Miniaturwelten)
                time.sleep(1.5)        # Kurze Pause
                st.session_state.page = 3
                st.rerun()

# ==========================================
# SEITE 3: Ergebnis (High Quality Look)
# ==========================================
elif st.session_state.page == 3:
    
    # Welches Bild nutzen wir als Hintergrund?
    bg_image = IMG_JUMPHOUSE if st.session_state.choice == "Jumphouse" else IMG_WUNDERLAND
    
    # Texte festlegen
    if st.session_state.choice == "Jumphouse":
        headline = "Alles klar. Jumphouse."
        subtext = "Pack die Sportsachen ein. Wir gehen springen. 🦘"
    else:
        headline = "Alles klar. Miniaturwunderland."
        subtext = "Gute Wahl. Bisschen Kultur und staunen. 🚂"

    # CSS für Seite 3: Bild als Hintergrund + Dunkles Overlay + Zentrierter Text
    st.markdown(f"""
    <style>
    .final-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url("{bg_image}");
        background-size: cover;
        background-position: center;
        filter: brightness(0.3); /* Macht das Bild dunkel damit Text lesbar ist */
        z-index: 0;
    }}
    
    .content-box {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 10;
        color: white;
        font-family: sans-serif;
        width: 80%;
    }}
    
    h1 {{
        font-size: 50px;
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    p {{
        font-size: 24px;
        font-weight: 300;
        color: #ddd;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # HTML rendern
    st.markdown('<div class="final-bg"></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="content-box">
            <h1>{headline}</h1>
            <p>{subtext}</p>
            <br>
            <p style="font-size: 16px; opacity: 0.7;">Ich schreib dir wann & wo.</p>
        </div>
    """, unsafe_allow_html=True)