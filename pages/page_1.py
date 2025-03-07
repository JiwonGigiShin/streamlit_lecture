import streamlit as st
import os

st.markdown("""
            # Welcome to Le Wagon
            """)

st.image(os.path.join(os.getcwd(),'raw_data', 'lw1.png'))

from PIL import Image

image = Image.open(os.path.join(os.getcwd(),'raw_data', 'lw2.png'))


if st.button('Logo 2?'):
    st.image(image)
