import os
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import requests

hf_url = "https://huggingface.co/aleisya01/cotton-leaf-diseases-and-pest-detection/resolve/main/model_cotton_leaf.h5"
output_model_path = "model_cotton_leaf.h5"

# Download model if not exists
if not os.path.exists(output_model_path):
    with st.spinner('Downloading model...'):
        r = requests.get(hf_url)
        with open(output_model_path, 'wb') as f:
            f.write(r.content)


# Load trained model
@st.cache_resource
def load_cnn_model():
    try:
        model = load_model(output_model_path)
        return model
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

model = load_cnn_model()
if model is None:
    st.stop()

# Class labels
class_names = ['Aphids', 'Army Worm', 'Bacterial Blight', 'Healthy', 'Powdery Mildew', 'Target Spot']

# App title
st.title("Cotton Leaf Disease & Pest Classifier 🌿")
st.write("Upload a cotton leaf image and let the model predict the condition or disease.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Display uploaded image
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption='Uploaded Leaf Image', use_column_width=True)

        # Preprocess image
        img_resized = img.resize((120, 120))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Predict
        predictions = model.predict(img_array)[0]
        sorted_indices = np.argsort(predictions)[::-1]

        st.subheader("Prediction Results:")
        for i in sorted_indices:
            st.write(f"{class_names[i]}: {predictions[i]*100:.2f}%")

        st.success(f"Top Prediction: {class_names[sorted_indices[0]]}")
    except Exception as e:
        st.error(f"Failed to process image: {e}")
