import streamlit as st
from utils.ui_components import apply_custom_styles, create_sidebar
from pages.home import show_home_page
from pages.classify import show_classification_page
from pages.about import show_about_page
from pages.model_info import show_model_info_page
import gdown
import os

# Set page configuration
st.set_page_config(
    page_title="Tea Leaf Disease Classifier",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="expanded"
)
model_path = "ensemble_model.h5"
if not os.path.exists(model_path):
    with st.spinner("Downloading model... please wait"):
        gdown.download("https://drive.google.com/uc?id=1klPO8ZwCk35TwPchgOi_2K57OnNU9nS0", model_path, quiet=False)
def main():
    
    # Remove Streamlit's default sidebar and header
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1rs6os {visibility: hidden;}
    .css-17ziqus {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Rest of your code continues...
    
    # Header
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='
            font-size: 3.5rem; 
            color: #2E8B57; 
            margin-bottom: 1rem;
            font-weight: 700;
        '>🍃 Tea Leaf Disease Classifier</h1>
        <h3 style='color: #3CB371; font-size: 1.5rem;'>
            AI-Powered Plant Health Analysis • Fast • Accurate • Reliable
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    app_mode = create_sidebar()
    
    # Route to appropriate page
    if app_mode == "Home":
        show_home_page()
    elif app_mode == "Classify Image":
        show_classification_page()
    elif app_mode == "About":
        show_about_page()
    elif app_mode == "Model Info":
        show_model_info_page()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #6c757d;'>"
        "© 2026 Tea Leaf Disease Classifier. All rights reserved."
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()