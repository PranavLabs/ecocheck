import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page Configuration
st.set_page_config(page_title="Eco-Gram AI", page_icon="🌱", layout="wide")

@st.cache_resource
def load_model():
    # Downloads the official YOLOv8s model weights
    return YOLO("yolov8s.pt") 

model = load_model()

# --- SUSTAINABILITY MATRIX ---
# Maps COCO dataset classes to environmental impact points
IMPACT_MAP = {
    # +++ HIGH POSITIVE (Natural Ecosystems)
    'bird': 15, 'cat': 5, 'dog': 5, 'horse': 10, 'sheep': 10, 'cow': 10, 
    'elephant': 20, 'bear': 15, 'zebra': 15, 'giraffe': 15, 'potted plant': 15,
    
    # + MODERATE POSITIVE (Sustainable/Public Infrastructure)
    'bicycle': 12, 'bench': 10, 'traffic light': 5, 'stop sign': 3, 'backpack': 2,
    
    # - MODERATE NEGATIVE (Electronic Waste & Consumption)
    'tv': -8, 'laptop': -10, 'mouse': -3, 'keyboard': -3, 'cell phone': -10, 
    'microwave': -12, 'oven': -12, 'refrigerator': -15, 'clock': -2, 'toaster': -10,
    
    # --- HIGH NEGATIVE (Pollution & Heavy Transport)
    'bottle': -15, 'cup': -10, 'wine glass': -10, 'fork': -5, 'knife': -5, 
    'spoon': -5, 'bowl': -5, 'car': -20, 'motorcycle': -15, 'bus': -12, 
    'truck': -25, 'boat': -15, 'airplane': -50
}

def analyze_vibe(found_labels):
    categories = {
        "Nature & Animals": ['bird', 'potted plant', 'dog', 'cat', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe'],
        "Green Transport": ['bicycle', 'bench'],
        "High Emission": ['car', 'motorcycle', 'bus', 'truck', 'boat', 'airplane'],
        "Waste & Plastic": ['bottle', 'cup', 'wine glass', 'fork', 'knife', 'spoon', 'bowl'],
        "Electronics": ['tv', 'laptop', 'mouse', 'keyboard', 'cell phone', 'microwave', 'oven', 'refrigerator', 'toaster']
    }
    return {cat: [l for l in found_labels if l in items] for cat, items in categories.items()}

# --- UI LAYOUT ---
st.title("🌱 Eco-Gram: Advanced Urban Auditor")
st.write("Scan images to analyze biodiversity vs. industrial footprint.")

uploaded_file = st.file_uploader("Upload an image (Instagram screenshot, street view, or room photo)...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    with st.spinner('AI analyzing environmental context...'):
        results = model(image)
        found_labels = [model.names[int(cls)] for cls in results[0].boxes.cls.tolist()]
        
        # Calculate Final Score
        score = 65 # Base neutral score
        for label in found_labels:
            score += IMPACT_MAP.get(label, 0)
        score = max(0, min(100, score))
        
        # UI Columns
        col_img, col_stats = st.columns([2, 1])
        
        with col_img:
            # Show the AI Bounding Boxes
            res_plotted = results[0].plot()
            st.image(res_plotted, caption="AI Object Detection", use_container_width=True)
            
        with col_stats:
            st.metric("Sustainability Score", f"{score}/100")
            
            # Display Category Breakdown
            st.write("### 📊 Findings")
            breakdown = analyze_vibe(found_labels)
            
            for cat, items in breakdown.items():
                if items:
                    st.write(f"**{cat}:** {len(items)} items")
                    st.caption(", ".join(set(items)))
            
            if 'person' in found_labels:
                st.warning("⚠️ **Privacy Alert:** Human subject detected. Impact data filtered for compliance.")
            
            # Actionable Advice
            st.divider()
            if score > 75:
                st.success("Verdict: High Biodiversity / Sustainable Zone.")
            elif score > 40:
                st.info("Verdict: Balanced Urban Environment.")
            else:
                st.error("Verdict: High Industrial / Waste Footprint.")
