import requests
import streamlit as st
st.title("Image Generation")
prompt="Generate a detailed diagram of the internal components of a solid-state lithium-ion battery cell"
url = "https://image.pollinations.ai/prompt/" + requests.utils.quote(prompt)
img=requests.get(url).content
with open("o.png", "wb") as f:
    f.write(img)
    st.image("o.png")
