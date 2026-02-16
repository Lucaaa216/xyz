import streamlit as st

# --- Konfiguration der Seite ---
st.set_page_config(
    page_title="Eine Frage an dich...",
    page_icon="💌",
    layout="centered"
)

# --- CSS für das Styling (Hintergrund & Zentrierung) ---
# Hier machen wir den Hintergrund hübsch (Verlauf) und zentrieren die Titel
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to top, #fad0c4 0%, #ffd1ff 100%);
    }
    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 18px;
    }
    p {
        font-size: 18px;
        text-align: center;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State Initialisierung ---
# Wir müssen speichern, auf welcher "Seite" wir sind
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'choice' not in st.session_state:
    st.session_state.choice = ""

# --- SEITE 1: Die Einleitung ---
if st.session_state.page == 1:
    
    # Platzhalter für vertikalen Abstand, damit es mittiger wirkt
    st.write("")
    st.write("")
    st.write("")
    
    st.title("Ich habe eine Frage an dich...")
    
    st.write("")
    st.write("")
    
    # Der Knopf
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Zur Frage ❤️"):
            st.session_state.page = 2
            st.rerun()

# --- SEITE 2: Die Auswahl ---
elif st.session_state.page == 2:
    
    st.title("Wo möchtest du mit mir hingehen?")
    st.write("")
    
    # Zwei Spalten (50% / 50%)
    col_left, col_right = st.columns(2)
    
    # --- Linke Seite: Jumphouse ---
    with col_left:
        # HINWEIS: Ersetze den Link unten durch den Dateinamen deines Bildes, 
        # wenn du ein lokales Bild hochlädst (z.B. "jumphouse.jpg")
        st.image("https://www.hamburg.de/resource/image/406012/landscape_ratio16x9/1240/697/13da6ae95443c66842a892d481476ca/867C02CEFA3C808D4962846D57A0774C/gallery-1-neuesstartbild.jpg", 
                 use_container_width=True, caption="Action pur!")
        
        st.write("") # Abstand
        if st.button("Zum Jumphouse 🦘"):
            st.session_state.choice = "Jumphouse"
            st.session_state.page = 3
            st.rerun()

    # --- Rechte Seite: Miniatur Wunderland ---
    with col_right:
        # HINWEIS: Hier Link zum Bild anpassen
        st.image("https://www.miniatur-wunderland.de/assets/content/layout/italien/italien-riomaggiore-highangle.jpg", 
                 use_container_width=True, caption="Kleine Welt ganz groß")
        
        st.write("") # Abstand
        if st.button("Zum Miniaturwunderland 🚂"):
            st.session_state.choice = "Wunderland"
            st.session_state.page = 3
            st.rerun()

# --- SEITE 3: Das Ergebnis (Optional, damit es nicht einfach stehen bleibt) ---
elif st.session_state.page == 3:
    st.balloons() # Konfetti-Effekt!
    st.title("Juhuu! 🎉")
    
    if st.session_state.choice == "Jumphouse":
        st.header("Dann hüpfen wir bald los! 🦘")
    else:
        st.header("Dann schauen wir uns die kleine Welt an! 🚂")
        
    st.write("")
    st.write("Ich freue mich drauf!")