import streamlit as st
import os

st.markdown("""# This is Page 3: Surprise!
""")


st.markdown("""
---
""")
if st.button('Surpise me 🎈🎈🎈!'):
    st.balloons()
    from PIL import Image
    image = Image.open(os.path.join(os.getcwd(), 'raw_data/lw1.png'))
    st.image(image, caption='Le Wagon!', use_column_width=False)
