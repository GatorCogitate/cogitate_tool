import streamlit as st
import numpy as np
import pandas as pd

    from PIL import Image
    image = Image.open('logo.png')

    st.image(image, caption='Welcome',
          use_column_width=True)
