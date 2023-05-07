import io
from PIL import Image
import streamlit as st
import time

#Defines columns for the before and after of the image
def columns(input_image,output_image):
    col1, col2 = st.columns(2)
    
    with col1:                          #Before 
            st.header("Before :pencil:")
            
            #Printing the image
            st.image(input_image)
            
            #converting PIL.JpegImagePlugin.JpegImageFile to Jpeg
            buffer = io.BytesIO()   
            input_image.save(buffer, format='JPEG', quality=75)
            
            #download button for before image
            btn = st.download_button(
            label="Download image :arrow_down:",
            data=buffer,
            file_name="sketch.png",
            mime="image/png"
            )

    with col2:                              #After
            st.header("After :lower_left_paintbrush:")
            
            #Progress bar
            progress_text = "Operation in progress. Please wait. :clock2:"
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.0075)
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty()
            
            #Printing the image
            st.image(output_image)
            
            #converting PIL.JpegImagePlugin.JpegImageFile to Jpeg
            output_buffer = io.BytesIO()   
            output_image.save(output_buffer, format='JPEG', quality=75)
            
            #download button for after image
            btn = st.download_button(
            label="Download image :arrow_down:",
            data=output_buffer,
            file_name="dress.png",
            mime="image/png"
            )
        