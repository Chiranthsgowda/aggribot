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
    /* Base styles */
    .stApp {
        background: linear-gradient(135deg, #3CB371, #2E8B57, #1E90FF);
    }
    
    /* Force responsive viewport */
    .main .block-container {
        max-width: 100% !important;
        padding-top: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    /* Typography - Mobile First */
    h1 {
        font-size: 1.8rem !important;
        text-align: center !important;
        margin: 0.5rem 0 !important;
        padding: 0 0.5rem !important;
        line-height: 1.2 !important;
        word-wrap: break-word !important;
    }
    
    h2 {
        font-size: 1rem !important;
        text-align: center !important;
        margin: 0.5rem 0 !important;
        padding: 0 0.5rem !important;
        line-height: 1.3 !important;
    }
    
    h3 {
        font-size: 1.1rem !important;
        text-align: center !important;
        margin: 1rem 0 !important;
        padding: 0 0.5rem !important;
    }
    
    /* Content containers */
    .centered-list {
        display: flex !important;
        justify-content: center !important;
        padding: 0.5rem !important;
        margin: 0.5rem auto !important;
        max-width: 95% !important;
        font-size: 0.85rem !important;
    }
    
    .centered-list ol {
        text-align: left !important;
        padding-left: 1rem !important;
        margin: 0 !important;
        display: inline-block !important;
    }
    
    .centered-list li {
        margin-bottom: 0.8rem !important;
        line-height: 1.4 !important;
        word-wrap: break-word !important;
    }
    
    .sideh {
        text-align: center !important;
        margin: 0.5rem auto !important;
        padding: 0 0.5rem !important;
        font-weight: bold !important;
        font-size: 0.9rem !important;
        max-width: 95% !important;
    }
    
    /* Images - Force responsive */
    .stImage > img {
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
    }
    
    /* Columns - Force single column on mobile */
    .stColumn {
        width: 100% !important;
        min-width: 0 !important;
        flex: none !important;
        margin-bottom: 1rem !important;
    }
    
    /* Sidebar adjustments */
    [data-testid="stSidebar"] {
        color: #222;
        font-family: 'Segoe UI', Arial, sans-serif;
        box-shadow: 0 4px 16px rgba(60,179,113,0.15);
    }
    
    /* Tablet styles */
    @media (min-width: 481px) and (max-width: 768px) {
        h1 {
            font-size: 2.2rem !important;
        }
        
        h2 {
            font-size: 1.2rem !important;
        }
        
        .centered-list {
            font-size: 0.9rem !important;
            max-width: 90% !important;
        }
        
        .sideh {
            font-size: 1rem !important;
        }
    }
    
    /* Desktop styles */
    @media (min-width: 769px) {
        h1 {
            font-size: 4.2rem !important;
        }
        
        h2 {
            font-size: 1.5rem !important;
        }
        
        h3 {
            font-size: 1.4rem !important;
        }
        
        .centered-list {
            font-size: 1rem !important;
            max-width: 80% !important;
            padding: 1.4rem !important;
        }
        
        .sideh {
            font-size: 1.5rem !important;
            padding-right: 4rem !important;
        }
        
        /* Desktop columns */
        .stColumn {
            width: 33.333% !important;
            flex: 1 !important;
            margin-bottom: 0 !important;
        }
    }
    
    /* Footer */
    .footer-text {
        font-size: 0.8rem !important;
        text-align: center !important;
        padding: 0 1rem !important;
        margin-top: 2rem !important;
    }
    
    hr {
        margin: 2rem 0 1rem 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown(
    """
    <div style="text-align: center;">
        <h1>🌾 Agriculture-Focused Chatbot 🌾</h1>
        <h2>Explore solutions and insights for agriculture, crops, and farming!</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <div class="sideh">
        Use the sidebar to switch between pages.
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

# Features section
st.markdown(
    """
    <h3>Explore Our Features</h3>
    """,
    unsafe_allow_html=True
)

# Images - will stack on mobile due to CSS
col1, col2, col3 = st.columns(3)

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

# Footer
st.markdown(
    """
    <hr>
    <div class="footer-text">
        🌱 Built with Streamlit & Google Gemini API 🌱
    </div>
    """,
    unsafe_allow_html=True
)
