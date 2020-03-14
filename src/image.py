import streamlit as st

from PIL import Image

image = Image.open("./images/logo.png")

st.image(image, use_column_width=True)

st.title("Welcome to Cogitate!")
st.text("Use the sidebar on the left to navigate through Cogitate's features.")
