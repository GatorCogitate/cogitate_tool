import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image

image = Image.open("./images/logo.png")

st.image(image, use_column_width=True)

st.title("Welcome to Cogitate!")
st.text("Use the sidebar on the left to navigate through Cogitate's features.")
