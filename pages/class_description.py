# Explanation.py
import streamlit as st

# Page settings
st.set_page_config(page_title="Explanation", layout="wide")

st.title("📖 Cotton Leaf Classes Explanation")

# Language toggle
language = st.radio("🌐 Choose Language / Pilih Bahasa:", ("English 🇬🇧", "Bahasa Indonesia 🇮🇩"))

# Class label descriptions
descriptions = {
    "Aphids": {
        "English": (
            "🪲 Aphids are tiny insects (1–3 mm) that feed by sucking plant sap, especially from the shoot tips and flowers. "
            "Their feeding causes leaves to wrinkle, yellow, and curl. More critically, aphids can transmit plant viruses."
        ),
        "Bahasa Indonesia": (
            "🪲 Aphids atau kutu daun adalah serangga kecil (1–3 mm) yang mengisap nutrisi tanaman dari pucuk tunas dan bunga. "
            "Daun menjadi keriput, menguning, dan terpuntir. Aphids juga dapat menyebarkan virus antar tanaman."
        )
    },
    "Army Worm": {
        "English": (
            "🐛 Army Worms (Spodoptera sp.) are caterpillars that eat plant leaves, starting with small holes and potentially "
            "destroying entire foliage, stems, and flowers."
        ),
        "Bahasa Indonesia": (
            "🐛 Army Worm (Spodoptera sp.) atau ulat gerayak adalah hama yang menyerang daun tanaman dan dapat memakan seluruh bagian "
            "daun hingga batang muda."
        )
    },
    "Bacterial Blight": {
        "English": (
            "🦠 Bacterial Blight is caused by *Xanthomonas campestris*. It starts as yellow spots that turn black and spread, "
            "killing leaf tissues and spreading via water splash."
        ),
        "Bahasa Indonesia": (
            "🦠 Bacterial Blight disebabkan oleh bakteri *Xanthomonas campestris*. Gejalanya berupa bercak kuning yang menjadi hitam dan menyebar, "
            "menyebabkan jaringan mati. Penyakit ini menyebar cepat melalui air hujan atau irigasi."
        )
    },
    "Healthy": {
        "English": (
            "🌱 This leaf is healthy, with no visible signs of disease or pest damage. Keep monitoring regularly!"
        ),
        "Bahasa Indonesia": (
            "🌱 Daun ini sehat tanpa tanda-tanda penyakit atau serangan hama. Tetap lakukan pemantauan secara rutin!"
        )
    },
    "Powdery Mildew": {
        "English": (
            "🍂 Powdery Mildew is a fungal disease that forms a white powder-like coating on the leaf surface. "
            "It spreads easily through air without free water."
        ),
        "Bahasa Indonesia": (
            "🍂 Powdery Mildew adalah penyakit jamur yang tampak seperti tepung putih di permukaan daun. "
            "Penyebarannya sangat mudah melalui udara tanpa membutuhkan air bebas."
        )
    },
    "Target Spot": {
        "English": (
            "🎯 Target Spot is caused by *Corynespora cassiicola*. It creates brown lesions that grow in size, "
            "drying out the infected parts of the leaf."
        ),
        "Bahasa Indonesia": (
            "🎯 Target Spot disebabkan oleh jamur *Corynespora cassiicola*. Bercak cokelat akan membesar dan menyebar, "
            "membuat bagian daun mengering dan mati."
        )
    }
}

# Show explanations
for label, texts in descriptions.items():
    with st.expander(label):
        st.markdown(texts["Bahasa Indonesia"] if "Indonesia" in language else texts["English"])
