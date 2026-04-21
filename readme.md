# 🌱 Eco-Check: Advanced Urban Sustainability Auditor

**Eco-Gram** is an AI-powered tool designed to quantify the environmental impact of urban spaces using computer vision. By analyzing images for biodiversity, transportation modes, and electronic waste, it generates a "Sustainability Score" to evaluate the ecological health of a captured scene.

[![Streamlit App](https://streamlit.io/images/brand/streamlit-mark-color.svg)](https://ecocheck.streamlit.app/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8s-green.svg)](https://github.com/ultralytics/ultralytics)

---

## 🚀 Key Features
- **80-Class Object Detection:** Powered by YOLOv8s to recognize everything from wildlife to industrial vehicles.
- **Dynamic Sustainability Matrix:** A custom weighted scoring system that rewards natural elements (+Nature) and penalizes high-emission or waste items (-Industrial).
- **Automated Urban Audit:** Provides a category-wise breakdown (Nature, Transport, Electronics, Waste) for deeper environmental insights.
- **Privacy-First Design:** Integrated "Privacy Alert" logic that flags human subjects for data compliance—crucial for cybersecurity-aware applications.

## 🛠️ Technical Stack
- **AI Framework:** Ultralytics YOLOv8
- **Frontend/Deployment:** Streamlit
- **Image Processing:** OpenCV & Pillow
- **Language:** Python

## 📊 How the Scoring Works
The model calculates a score from **0-100** based on detected classes:
- **+15 Points:** Biodiversity markers (Birds, Trees/Plants, Wildlife).
- **+10 Points:** Sustainable infrastructure (Bicycles, Benches).
- **-20 Points:** Heavy emissions (Trucks, Cars, Airplanes).
- **-15 Points:** Potential waste (Plastic bottles, Disposable cups).

## 📦 Installation & Local Setup

If you want to run this on your local machine (e.g., **Acer Aspire 7** with **GTX 1650**), follow these steps:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/eco-gram-ai.git](https://github.com/yourusername/eco-gram-ai.git)
   cd eco-gram-ai
