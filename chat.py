import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Gen Ai")
prompt=st.text_input("Enter the content")
a="A GenAI-based system that automatically detects harmful content and provides clear, human-readable explanations for moderation decisions."
response=model.generate_content(prompt+a)
st.write(response.text) 
