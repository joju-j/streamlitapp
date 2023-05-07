import streamlit as st
from PIL import Image
from io import StringIO
from sidebar import sidebar  
from transform import sketch2fashion

# to run type python3.11 -m streamlit run main.py

#Invokes sidebar and details
sidebar()

st.title(':red[Generating Clothing Visualization Using Sketches] :dress:')
st.subheader('Upload your sketch here or take a picture to see the results:exclamation::exclamation:')

uploaded_file = st.file_uploader(" ", type=['jpg','png','jpeg'])

picture = st.camera_input("Take a picture ! :camera_with_flash:")

if picture is not None and uploaded_file is None:
    #Sends picture to backend and preprocess
    sketch2fashion(picture,1)


if uploaded_file is not None and picture is None:    
    #To download to system:
    # with open(os.path.join("C:/Users/hp/streamlit-test/",uploaded_file.name),"wb") as f:
    #        f.write(uploaded_file.getbuffer())
    sketch2fashion(uploaded_file,1)