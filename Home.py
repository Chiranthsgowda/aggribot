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
    
    /* Mobile-first responsive design */
    .centered-list {
        display: flex;
        justify-content: center;
        text-align: left;
        padding: 1rem;
        font-size: 1rem;
        margin: 0 auto;
        max-width: 90%;
    }
    
    .sideh {
        display: flex;
        justify-content: center;
        text-align: center;
        margin: 1rem auto;
        padding: 0 1rem;
        font-weight: bold;
        font-size: 1.2rem;
        max-width: 90%;
    }
    
    .stimage {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 1rem;
    }
    
    /* Responsive headings */
    h1 {
        font-size: 3rem !important;
        text-align: center;
        margin: 1rem 0 !important;
        padding: 0 1rem;
        line-height: 1.2 !important;
    }
    
    h2 {
        font-size: 1.3rem !important;
        text-align: center;
        margin: 1rem 0 !important;
        padding: 0 1rem;
        line-height: 1.3 !important;
    }
    
    h3 {
        font-size: 1.4rem !important;
        text-align: center;
        margin: 1.5rem 0 !important;
        padding: 0 1rem;
    }
    
    /* Mobile-specific styles */
    @media (max-width: 768px) {
        h1 {
            font-size: 2.2rem !important;
            padding: 0 0.5rem;
        }
        
        h2 {
            font-size: 1.1rem !important;
            padding: 0 0.5rem;
        }
        
        h3 {
            font-size: 1.2rem !important;
            padding: 0 0.5rem;
        }
        
        .sideh {
            font-size: 1rem;
            padding: 0 0.5rem;
            margin: 0.5rem auto;
        }
        
        .centered-list {
            padding: 0.5rem;
            font-size: 0.9rem;
            max-width: 95%;
        }
        
        .centered-list ol {
            padding-left: 1.2rem;
        }
        
        .centered-list li {
            margin-bottom: 0.8rem;
            line-height: 1.4;
        }
        
        /* Adjust columns for mobile */
        .stColumn {
            padding: 0.25rem !important;
        }
        
        /* Image responsiveness */
        .stImage img {
            max-width: 100% !important;
            height: auto !important;
        }
        
        /* Footer adjustments */
        hr {
            margin: 2rem 0 1rem 0 !important;
        }
        
        .footer-text {
            font-size: 0.8rem !important;
            padding: 0 1rem;
        }
    }
    
    /* Very small screens */
    @media (max-width: 480px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2 {
            font-size: 1rem !important;
        }
        
        .sideh {
            font-size: 0.9rem;
        }
        
        .centered-list {
            font-size: 0.85rem;
            max-width: 98%;
        }
        
        .centered-list ol {
            padding-left: 1rem;
        }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        color: #222;
        font-family: 'Segoe UI', Arial, sans-serif;
        box-shadow: 0 4px 16px rgba(60,179,113,0.15);
    }
    
    [data-testid="stSidebar"] .css-1v0mbdj, 
    [data-testid="stSidebar"] .css-1lcbmhc {
        color: #222 !important;
        font-weight: bold;
    }
    
    /* Responsive container */
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page with responsive container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

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
                <li><b>Prompt Solutions</b> – ask agricultural questions and get detailed answers.</li>
                <li><b>Report Analysis</b> – upload PDFs to summarize, extract themes, or sanity-check claims.</li>
                <li><b>Crop Advice</b> – get soil/region-specific guidance for your crop.</li>
            </ol>
        </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --- Images Section with Responsive Layout ---
st.markdown(
    """
    <h3 style="text-align: center;">Explore Our Features</h3>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Create responsive columns that stack on mobile
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.image(
        "src/prompt.png",
        caption="Get instant answers to your agriculture queries.",
        use_container_width=True
    )

with col2:
    st.image(
        "src/report.png",
        caption="Analyze reports and extract key information.",
        use_container_width=True 
    )

with col3:
    st.image(
        "src/advice.png",
        caption="Receive tailored crop advice based on your region.",
        use_container_width=True
    )

st.markdown(
    """
    <hr>
    <p class="footer-text" style="text-align:center; font-size:0.9rem;">
        🌱 Built with Streamlit & Google Gemini API 🌱
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-content div
