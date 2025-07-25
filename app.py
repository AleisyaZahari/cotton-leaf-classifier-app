import os
import gdown
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Page Settings
st.set_page_config(page_title="Cotton Leaf Classifier", layout="wide")

# Header
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h1 style='color: green; font-size: 40px;'>🌿 Cotton Leaf Diseases & Pests Classifier</h1>
        <p style='font-size: 18px;'>Detect cotton leaf diseases and pests using AI!</p>
        <p style='font-size: 16px;'>Upload a cotton leaf image, and the model will identify the disease or pest.</p>
        <hr style='border-top: 2px solid #bbb;'/>
    </div>
""", unsafe_allow_html=True)
# Language selector
# language = st.radio("🌐 Choose Language / Pilih Bahasa:", ("English 🇬🇧", "Bahasa Indonesia 🇮🇩"))

# Download model from Google Drive
file_id = '1waADn53Sa3aFKOfNSyKvCo9l8-Tn5CvF'
output_model_path = 'model_cotton_leaf.h5'
gdrive_url = f'https://drive.google.com/uc?id={file_id}'

if not os.path.exists(output_model_path):
    with st.spinner('🔽 Downloading model from Google Drive...'):
        gdown.download(gdrive_url, output_model_path, quiet=False)

@st.cache_resource
def load_cnn_model():
    try:
        return load_model(output_model_path)
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

model = load_cnn_model()
if model is None:
    st.stop()

# Class labels and descriptions
class_names = ['Aphids', 'Army Worm', 'Bacterial Blight', 'Healthy', 'Powdery Mildew', 'Target Spot']
# Class labels and detailed descriptions
class_descriptions = {
    'Aphids': (
        "🪲 Aphids are tiny insects (1–3 mm) that feed by sucking plant sap, especially from the shoot tips and flowers. "
        "Their feeding causes leaves to wrinkle, yellow, and curl. More critically, aphids can transmit plant viruses, "
        "posing a serious threat to healthy crops. Rapid identification and control are essential to prevent yield losses."
    ),
    'Army Worm': (
        "🐛 Army Worms (Spodoptera sp.) are destructive pests that attack mainly the leaves of plants. They begin damaging "
        "during the larval stage by creating holes in the leaves and, as they mature, can devour entire leaf surfaces, "
        "young shoots, flowers, and even stems. Their population surges during the rainy season and requires immediate management."
    ),
    'Bacterial Blight': (
        "🦠 Bacterial Blight is caused by *Xanthomonas campestris pv. malvacearum*. It appears as yellow spots that turn "
        "dark brown or black, spreading along the leaf veins and leading to widespread tissue death. The disease spreads "
        "rapidly through splashing water, wind-driven rain, or irrigation. Early detection and control are crucial."
    ),
    'Healthy': (
        "🌱 This cotton leaf appears healthy with no visible signs of disease or pest infestation. Regular monitoring is "
        "recommended to maintain plant health and detect any early signs of damage."
    ),
    'Powdery Mildew': (
        "🍂 Powdery Mildew is a fungal disease that forms a white, powdery layer on the leaf surface. It spreads easily "
        "without needing free water, making it highly contagious. Caused by airborne spores, this disease weakens the plant "
        "by affecting photosynthesis. Early detection helps limit its spread."
    ),
    'Target Spot': (
        "🎯 Target Spot is caused by the fungus *Corynespora cassiicola*, forming brown lesions that expand progressively. "
        "These spots often have a dark center and may dry out and kill the infected areas. Severe infections can cause leaf "
        "drop and significantly reduce crop yield."
    )
}


# Upload Section
st.markdown("### 📤 Upload Your Image")
uploaded_file = st.file_uploader("Choose a cotton leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        col1, col2 = st.columns([1, 2])

        with col1:
            img = Image.open(uploaded_file).convert("RGB")
            st.image(img, caption='🖼️ Uploaded Image', use_column_width=True)

        # Preprocess
        img_resized = img.resize((120, 120))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Predict
        predictions = model.predict(img_array)[0]
        sorted_indices = np.argsort(predictions)[::-1]
        top_idx = sorted_indices[0]

        with col2:
            st.markdown("### 🔍 Prediction Results")
            for i in sorted_indices:
                st.markdown(f"""
                    <div style="font-size:18px; padding-left: 10px;">
                        🔹 <b>{class_names[i]}</b>: <code>{predictions[i]*100:.2f}%</code>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style="background-color:#e6ffe6; padding:15px; border-left:5px solid green; margin-top:20px;">
                    ✅ <b>Most Likely:</b> <span style="font-size:22px;">{class_names[top_idx]}</span>
                </div>
            """, unsafe_allow_html=True)

        # Explanation
        top_class = class_names[top_idx]
        description = class_descriptions.get(top_class, "No description available.")

        st.markdown(f"""
            <hr style='border-top: 2px dashed #ccc;'/>
            <div style="background-color:#f1f1f1; padding:20px; border-radius:10px;">
                <h4>📖 Explanation</h4>
                <p style="font-size:16px;">{description}</p>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error: {e}")
