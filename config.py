# Configuration and constants

# Class names mapping
CLASS_NAMES = {
    0: "Tea algal leaf spot",
    1: "Brown Blight", 
    2: "Gray Blight",
    3: "Helopeltis",
    4: "Red spider",
    5: "Green mirid bug",
    6: "Healthy",
}

# Model paths
MODEL_PATHS = [
    'models/ensemble_model.h5',
    './models/ensemble_model.h5', 
    'ensemble_model.h5',
    './ensemble_model.h5'
]

# Image settings
TARGET_SIZE = (224, 224)

# Disease information
DISEASE_INFO = {
    "Tea algal leaf spot": {
        "description": "Caused by algae, appears as reddish-brown or orange spots on leaf surfaces. Common in humid conditions.",
        "symptoms": ["Reddish-brown spots", "Orange discoloration", "Leaf surface damage"],
        "severity": "Medium"
    },
    "Brown Blight": {
        "description": "Fungal infection causing brown spots that can expand and cause leaf blight. Affects leaf quality.",
        "symptoms": ["Brown spots", "Leaf blight", "Tissue damage"],
        "severity": "High"
    },
    "Gray Blight": {
        "description": "Fungal disease with grayish mold growth, typically appearing in humid and shaded conditions.",
        "symptoms": ["Gray mold", "Fungal growth", "Leaf discoloration"],
        "severity": "Medium"
    },
    "Helopeltis": {
        "description": "Insect damage caused by Helopeltis bugs, creating small necrotic spots on leaves.",
        "symptoms": ["Necrotic spots", "Insect damage", "Leaf punctures"],
        "severity": "Medium"
    },
    "Red spider": {
        "description": "Caused by spider mites, resulting in yellowing or bronzing of leaves with fine webbing.",
        "symptoms": ["Yellowing leaves", "Fine webbing", "Bronze discoloration"],
        "severity": "High"
    },
    "Green mirid bug": {
        "description": "Insect damage from green mirid bugs causing punctures and deformations on leaves.",
        "symptoms": ["Leaf punctures", "Deformations", "Insect activity"],
        "severity": "Low"
    },
    "Healthy": {
        "description": "The tea leaf appears healthy with no signs of common diseases or pest damage.",
        "symptoms": ["Normal coloration", "No spots or lesions", "Healthy growth"],
        "severity": "None"
    }
}