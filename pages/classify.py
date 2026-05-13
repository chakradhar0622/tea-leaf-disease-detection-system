import streamlit as st
from PIL import Image
from utils.model_utils import load_ensemble_model, predict_disease
from utils.image_utils import preprocess_image
from utils.ui_components import display_prediction_results

def show_classification_page():
    """Display the image classification interface"""
    
    st.markdown("""
    <div class='custom-card'>
        <h2>📸 Upload Tea Leaf Image</h2>
        <p>Upload a clear image of a tea leaf for AI-powered disease detection and analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "**Drag and drop or click to upload**",
        type=['jpg', 'jpeg', 'png', 'bmp'],
        help="Supported formats: JPG, JPEG, PNG, BMP",
        key="classify_uploader"
    )
    
    if uploaded_file is not None:
        # Create two columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Image preview with card styling
            st.markdown("""
            <div class='custom-card'>
                <h3>🖼️ Image Preview</h3>
            """, unsafe_allow_html=True)
            
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Tea Leaf", use_column_width=True)
                
                # Image metadata
                st.markdown("**📊 Image Details**")
                col_img1, col_img2 = st.columns(2)
                with col_img1:
                    st.metric("Format", uploaded_file.type.split('/')[-1].upper())
                    st.metric("Width", f"{image.size[0]}px")
                with col_img2:
                    st.metric("Size", f"{uploaded_file.size / 1024:.1f} KB")
                    st.metric("Height", f"{image.size[1]}px")
                
            except Exception as e:
                st.error(f"❌ Error loading image: {e}")
                return
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            # Analysis results section
            st.markdown("""
            <div class='custom-card'>
                <h3>🔬 Analysis Results</h3>
            """, unsafe_allow_html=True)
            
            # Load model with progress
            with st.spinner("🔄 Loading AI model..."):
                model = load_ensemble_model()
            
            if model is not None:
                # Preprocess image
                with st.spinner("🔄 Processing image..."):
                    try:
                        processed_image = preprocess_image(image)
                    except Exception as e:
                        st.error(f"❌ {e}")
                        return
                
                if processed_image is not None:
                    # Make prediction with progress
                    with st.spinner("🧠 Analyzing tea leaf..."):
                        predictions = predict_disease(model, processed_image)
                    
                    if predictions is not None:
                        display_prediction_results(predictions)
                    else:
                        st.error("❌ Prediction failed. Please try another image.")
            else:
                st.error("❌ Model not available. Please check the model file.")
            
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("👆 Please upload a tea leaf image to get started with the analysis.")