import streamlit as st

def show_about_page():
    """Display about page"""
    
    st.markdown("""
    <div class='custom-card'>
        <h2>🌿 About Tea Leaf AI</h2>
        <p>Advanced AI-powered solution for tea leaf disease detection and agricultural health monitoring.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mission and vision
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='custom-card'>
            <h3>🎯 Our Mission</h3>
            <p>To empower farmers and agricultural professionals with accessible, 
            accurate AI tools for plant disease detection and crop health management.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='custom-card'>
            <h3>👁️ Our Vision</h3>
            <p>Creating a future where AI-assisted agriculture helps ensure 
            food security and sustainable farming practices worldwide.</p>
        </div>
        """, unsafe_allow_html=True)