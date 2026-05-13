import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from config import MODEL_PATHS

@st.cache_resource(show_spinner=False)
def load_ensemble_model():
    """Load the ensemble model with comprehensive error handling"""
    try:
        model = None
        for path in MODEL_PATHS:
            try:
                if os.path.exists(path):
                    st.info(f"Loading model from: {path}")
                    model = load_model(path)
                    break
            except Exception as e:
                continue
        
        if model is None:
            st.error("""
            ❌ Model file not found. Please ensure:
            - The model file 'ensemble_model.h5' is in the 'models' folder
            """)
            return None
            
        st.success("✅ Model loaded successfully!")
        return model
        
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

def predict_disease(model, image_array):
    """Make prediction using the ensemble model"""
    try:
        predictions = model.predict(image_array, verbose=0)
        return predictions[0]
    except Exception as e:
        st.error(f"❌ Error making prediction: {e}")
        return None