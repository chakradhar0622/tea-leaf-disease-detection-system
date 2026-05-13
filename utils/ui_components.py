import streamlit as st
import pandas as pd
import numpy as np
from config import CLASS_NAMES, DISEASE_INFO

def apply_custom_styles():
    """Apply custom CSS styles"""
    try:
        with open('assets/styles.css', 'r') as f:
            css = f.read()
            st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback to inline CSS if file not found
        st.markdown("""
        <style>
        .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
        .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
        .custom-card {
            background: white; padding: 25px; border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #2E8B57;
            margin: 15px 0;
        }
        </style>
        """, unsafe_allow_html=True)

def create_sidebar():
    """Create the application sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h1 style='color: white; margin-bottom: 30px;'>🍃 Tea AI</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        app_mode = st.selectbox(
            "Choose a page",
            ["🏠 Home", "🔍 Classify Image", "ℹ️ About", "🤖 Model Info"],
            label_visibility="collapsed"
        )
        
        # Clean up the mode for internal use
        app_mode_clean = app_mode.replace("🏠 ", "").replace("🔍 ", "").replace("ℹ️ ", "").replace("🤖 ", "")
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Classes", "7")
        with col2:
            st.metric("Models", "3")
        
        return app_mode_clean

def display_prediction_results(predictions):
    """Display the prediction results with enhanced UI"""
    predicted_class = np.argmax(predictions)
    confidence = predictions[predicted_class]
    disease_name = CLASS_NAMES.get(predicted_class, "Unknown")
    
    # Display results
    if disease_name == "Healthy":
        st.success(f"🎉 **Diagnosis: {disease_name}** (Confidence: {confidence:.2%})")
        st.info("Great news! This tea leaf appears to be healthy and free from common diseases.")
    else:
        st.error(f"⚠️ **Diagnosis: {disease_name}** (Confidence: {confidence:.2%})")
        st.warning("This leaf shows signs of potential issues. Consult with agricultural experts.")
    
    # Display confidence scores
    display_confidence_scores(predictions, disease_name)
    
    # Display disease information if not healthy
    if disease_name != "Healthy":
        display_disease_info(disease_name)

def display_confidence_scores(predictions, top_disease):
    """Display confidence scores for all classes"""
    st.markdown("### 📊 Confidence Distribution")
    
    # Create dataframe for better display
    results_df = pd.DataFrame({
        'Condition': [CLASS_NAMES[i] for i in range(len(CLASS_NAMES))],
        'Confidence': predictions
    })
    results_df = results_df.sort_values('Confidence', ascending=False)
    
    # Display confidence bars
    for _, row in results_df.iterrows():
        confidence_pct = row['Confidence'] * 100
        condition = row['Condition']
        is_predicted = condition == top_disease
        
        # Create a progress bar-like display
        st.write(f"**{condition}:** {confidence_pct:.1f}%")
        st.progress(float(row['Confidence']))

def display_disease_info(condition_name):
    """Display information about the detected condition"""
    info = DISEASE_INFO.get(condition_name, {
        "description": "Comprehensive information being updated.",
        "symptoms": ["Information updating"],
        "severity": "Unknown"
    })
    
    st.markdown("### ℹ️ Disease Information")
    
    st.write(f"**Description:** {info['description']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Symptoms:**")
        for symptom in info["symptoms"]:
            st.write(f"- {symptom}")
    
    with col2:
        st.write("**Severity:**")
        severity_color = {
            "Low": "🟢",
            "Medium": "🟡", 
            "High": "🔴",
            "Unknown": "⚫"
        }
        st.write(f"{severity_color.get(info['severity'], '⚫')} {info['severity']}")