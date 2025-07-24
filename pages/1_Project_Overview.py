import streamlit as st

st.title("📄 Project Overview")
st.header("Classification of Cotton Leaf Diseases and Pests Using CNN")

st.subheader("Overview")
st.write("""
This project aims to classify cotton leaf diseases and pests using a Convolutional Neural Network (CNN). 
The model is built from scratch to assist farmers in detecting plant diseases and pests early, achieving a classification accuracy of 91%.
""")

st.subheader("Author")
st.markdown("""
**Aleisya Zahari Salam**  
Department of Mathematics, Faculty of Mathematics and Natural Sciences, Universitas Pamulang  
**Research Advisor:** Yulianti Rusdiana, S.Si., M.Sc.
""")

st.subheader("Abstract")
st.write("""
Cotton is essential for the textile and food industries, making its cultivation a priority. However, it is susceptible to various diseases and pests that affect crop yields. Manual identification is often inaccurate and time-consuming, necessitating a more efficient solution.
""")

# And so on... you can use st.markdown(), st.write(), st.latex() if needed

st.subheader("Dataset")
st.markdown("""
- **Diseases**: Bacterial Blight, Powdery Mildew, Target Spot  
- **Pests**: Aphids, Army Worm  
- **Healthy Leaves**
""")

st.subheader("Results")
st.write("Using the CNN method, the classification results were:")
st.markdown("""
- Aphids: 58 correctly classified, 7 misclassified  
- Army Worm: 56 correctly classified, 4 misclassified  
- Healthy Leaves: 60 correctly classified (100% accuracy)  
- Bacterial Blight: 53 correctly classified, 7 misclassified  
- Target Spot: 52 correctly classified, 9 misclassified  
- **Final Accuracy**: 91%
""")

st.subheader("Future Work")
st.markdown("""
- Expand the dataset to include more disease and pest types  
- Explore transfer learning (e.g., YOLO, ResNet)  
- Deploy as mobile/web app for real-time use by farmers
""")
st.subheader("Connect with Me")
st.markdown("""
🔗 [Main Project Repository](https://github.com/AleisyaZahari/Classification-Cotton-Leaf-Pests-and-Diseases)  
🔗 [Streamlit App Repository](https://github.com/AleisyaZahari/cotton-leaf-classifier-app)  
👩‍💼 [LinkedIn Profile](https://www.linkedin.com/in/aleisyazaharisalam/)
""")
