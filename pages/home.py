import streamlit as st
from config import CLASS_NAMES

def show_home_page():
    
    """Display the home page"""
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='custom-card'>
            <h2>🌿 Welcome to Tea Leaf AI</h2>
            <p>Advanced AI-powered tea leaf disease detection system that helps farmers 
            and agricultural experts identify plant health issues with remarkable accuracy.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features grid
        st.subheader("🚀 Key Features")
        features_col1, features_col2, features_col3 = st.columns(3)
        
        with features_col1:
            st.markdown("""
            <div class='custom-card' style='text-align: center;'>
                <h3>🎯</h3>
                <h4>High Accuracy</h4>
                <p>Ensemble model combining multiple architectures</p>
            </div>
            """, unsafe_allow_html=True)
            
        with features_col2:
            st.markdown("""
            <div class='custom-card' style='text-align: center;'>
                <h3>⚡</h3>
                <h4>Fast Analysis</h4>
                <p>Real-time processing of tea leaf images</p>
            </div>
            """, unsafe_allow_html=True)
            
        with features_col3:
            st.markdown("""
            <div class='custom-card' style='text-align: center;'>
                <h3>📊</h3>
                <h4>Detailed Insights</h4>
                <p>Comprehensive reports with confidence scores</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Quick start card
        st.markdown("""
        <div class='custom-card'>
            <h3>🔍 Quick Start</h3>
            <ol style='padding-left: 20px;'>
                <li>Go to <b>Classify Image</b></li>
                <li>Upload tea leaf photo</li>
                <li>Get instant diagnosis</li>
                <li>View recommendations</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Supported conditions
        st.markdown("""
        <div class='custom-card'>
            <h3>🌱 Supported Conditions</h3>
        """, unsafe_allow_html=True)
        
        for class_name in CLASS_NAMES.values():
            emoji = "✅" if class_name == "Healthy" else "🦠"
            st.write(f"{emoji} {class_name}")
        
        st.markdown("</div>", unsafe_allow_html=True)