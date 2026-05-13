import streamlit as st

def show_model_info_page():
    """Display model information page"""
    
    st.markdown("""
    <div class='custom-card'>
        <h2>🤖 Model Architecture</h2>
        <p>Advanced ensemble learning approach combining multiple deep learning models for superior accuracy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model cards
    st.subheader("🧠 Ensemble Components")
    
    model_cols = st.columns(3)
    
    models_info = [
        {
            "name": "Custom CNN",
            "emoji": "🔄",
            "description": "Lightweight convolutional neural network optimized for tea leaf analysis",
            "specs": ["Input: 128×128 pixels", "Fast inference", "Custom architecture"]
        },
        {
            "name": "VGG16",
            "emoji": "🏗️", 
            "description": "Pre-trained VGG16 with transfer learning for feature extraction",
            "specs": ["Input: 224×224 pixels", "ImageNet weights", "Strong features"]
        },
        {
            "name": "DenseNet",
            "emoji": "🕸️",
            "description": "DenseNet architecture with dense connections for feature reuse",
            "specs": ["Input: 128×128 pixels", "Dense blocks", "Parameter efficient"]
        }
    ]
    
    for i, model_info in enumerate(models_info):
        with model_cols[i]:
            st.markdown(f"""
            <div class='custom-card'>
                <div style='text-align: center; margin-bottom: 15px;'>
                    <h1>{model_info['emoji']}</h1>
                    <h3>{model_info['name']}</h3>
                </div>
                <p>{model_info['description']}</p>
                <ul>
            """, unsafe_allow_html=True)
            
            for spec in model_info['specs']:
                st.markdown(f"<li>{spec}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)