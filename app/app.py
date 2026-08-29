import streamlit as st
import pandas as pd
import numpy as np
import re # which gives you access to regex functions
import preprocessor as preprocessor

st.sidebar.title("WhatsApp Chat Analyser")

# insert file uploader to upload the chat file
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt"]) 
if uploaded_file is not None:
    # read the file
    data = uploaded_file.read().decode("utf-8")
    st.text_area("Chat Data", data, height=300)

    df = preprocessor.preprocess_chat_data(data)