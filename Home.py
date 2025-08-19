import streamlit as st

st.set_page_config(
    page_title="Agribot",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #3CB371, #2E8B57, #1E90FF);
    }
    .centered-list {
        display: flex;
        justify-content: center;
        text-align: left;
        padding-top: 1.4rem;
        font-size: 1rem;

    }
    .sideh {
        display: flex;
        justify-content: center;
        text-align: center;
        margin-right: auto;
        padding-right: 4rem;
        font-weight: bold;
        font-size: 1.5rem;
    }
    .stimage {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 1rem;
    }
    h1 {
        font-size: 4.2rem !important;
        text-align: center;
    }
    @media (max-width: 768px) {
        h1 
        { 
            font-size: 2.5rem !important; 
        }
    }
    h2 {
        font-size: 1.5rem !important;
        text-align: center;
    }
    [data-testid="stSidebar"] {
        color: #222;
        font-family: 'Segoe UI', Arial, sans-serif;
        box-shadow: 0 4px 16px rgba(60,179,113,0.15);
        max-width: 1px;
    }
    [data-testid="stSidebar"] .css-1v0mbdj, [data-testid="stSidebar"] .css-1lcbmhc {
        color: #222 !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Home Page
st.markdown(
    """
    <div style="text-align: center;">
        <h1>🌾 Agriculture-Focused Chatbot 🌾</h1>
        <h2>Explore solutions and insights for agriculture, crops, and farming!</h2>
        <br>
        <p class="sideh">Use the sidebar to switch between pages.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <div class="sideh">
            <b>This app has three features:</b>
    </div>
    """, 
    unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="centered-list">     
            <ol>
                <li><b>Prompt Solutions</b> – ask agricultural questions and get detailed answers .</li>
                <li><b>Report Analysis</b> – upload PDFs to summarize, extract themes, or sanity-check claims.</li>
                <li><b>Crop Advice</b> – get soil/region-specific guidance for your crop.</li>
            </ol>
        </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True) # Adds a little space

# --- Images Below Features ---
# Use st.columns to create three equally spaced columns
st.markdown("<br>", unsafe_allow_html=True)  # Adds a little space

st.markdown(
    """
    <h3 style="text-align: center;">Explore Our Features</h3>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True) # Adds a little space

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "aggribot/src/prompt.png",
        caption="Get instant answers to your agriculture queries.",
        width=340,  
        use_container_width=True
    )

with col2:
    st.image(
        "aggribot/src/report.png",
        caption="Analyze reports and extract key information.",
        width=340, 
        use_container_width=True 
    )

with col3:
    st.image(
        "aggribot/src/advice.png",
        caption="Receive tailored crop advice based on your region.",
        width=340,  
        use_container_width=True
    )

st.markdown(
    """
    <hr>
    <p style="text-align:center; font-size:0.9rem;">
        🌱 Built with Streamlit & Google Gemini API 🌱
    </p>
    """,
    unsafe_allow_html=True
)
