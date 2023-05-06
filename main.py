import streamlit as st
from PIL import Image
from io import StringIO
import os
import urllib
import urllib.request
# to run type python3.11 -m streamlit run main.py

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.png'
    urllib.request.urlretrieve(url, full_path)

st.title(':red[Generating Clothing Visualization Using Sketches] :dress:')
st.subheader('Upload your sketch here or take a picture to see the results:exclamation::exclamation:')

uploaded_file = st.file_uploader(" ", type=['jpg','png','jpeg'])

picture = st.camera_input("Take a picture")

if picture is not None and uploaded_file is None:
    # with open(os.path.join("C:/Users/hp/streamlit-test/",picture.name),"wb") as f:
        #  f.write(picture.getbuffer())
    col1, col2 = st.columns(2)
    with col1:
        st.header("Before")
        st.image(picture)  
       
        btn = st.download_button(
         label="Download image",
         data=picture,
         file_name="sketch.png",
         mime="image/png"
        )
    with col2:
        st.header("After")

if uploaded_file is not None and picture is None:
    image = Image.open(uploaded_file)
    # with open(os.path.join("C:/Users/hp/streamlit-test/",uploaded_file.name),"wb") as f:
        #  f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)
    with col1:
        st.header("Before")
        st.image(image)  

    with col2:
        st.header("After")
