import streamlit as st
import numpy as np
import pandas as pd

    from PIL import Image
    image = Image.open('sunrise.jpg')

    st.image(image, caption='Sunrise by the mountains',
          use_column_width=True)
