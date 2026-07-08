import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="")
model = genai.GenerativeModel('gemini-2.5-flash')
st.title("image ai")
a=st.file_uploader("upload an image",type=["jpg","jpeg","png"])
prompt=st.text_input("enter the question")
if st.button('submit'):
    img = Image.open(a)
    response = model.generate_content([img,prompt])
    st.write(response.text)
