import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PROMETHEUS-X",
    page_icon="🔍"
)

st.title("PROMETHEUS-X")
st.subheader("Industrial Anomaly Detection System")

st.write(
    "Detect unknown, rare and unseen "
    "industrial defects using Computer Vision."
)

uploaded_file = st.file_uploader(
    "Upload Industrial Product Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Product")
    st.success("Image uploaded successfully!")