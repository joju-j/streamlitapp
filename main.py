import streamlit as st
from PIL import Image
from io import StringIO
import os
import urllib
import urllib.request
import time
import importlib
from sidebar import sidebar  

# to run type python3.11 -m streamlit run main.py
sidebar()

st.title(':red[Generating Clothing Visualization Using Sketches] :dress:')
st.subheader('Upload your sketch here or take a picture to see the results:exclamation::exclamation:')

uploaded_file = st.file_uploader(" ", type=['jpg','png','jpeg'])

picture = st.camera_input("Take a picture ! :camera_with_flash:")

if picture is not None and uploaded_file is None:
    # with open(os.path.join("C:/Users/hp/streamlit-test/",picture.name),"wb") as f:
        #  f.write(picture.getbuffer())
    col1, col2 = st.columns(2)
    with col1:
        st.header("Before :pencil:")
        st.image(picture)  
       
        btn = st.download_button(
         label="Download image :arrow_down:",
         data=picture,
         file_name="sketch.png",
         mime="image/png"
        )
    with col2:
        st.header("After :lower_left_paintbrush:")
        progress_text = "Operation in progress. Please wait. :clock2:"
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        btn = st.download_button(
            label="Download image :arrow_down:",
            data=picture,
            file_name="dress.png",
            mime="image/png"
            )


if uploaded_file is not None and picture is None:
    image = Image.open(uploaded_file)
    # with open(os.path.join("C:/Users/hp/streamlit-test/",uploaded_file.name),"wb") as f:
        #  f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)
    with col1:
        st.header("Before :pencil:")
        st.image(image)  

    with col2:
        st.header("After :lower_left_paintbrush:")
        progress_text = "Operation in progress. Please wait. :clock2:"
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        btn = st.download_button(
            label="Download image :arrow_down:",
            data=uploaded_file,
            file_name="dress.png",
            mime="image/png"
            )
