import streamlit as st
import pandas as pd
import numpy as np
import re # which gives you access to regex functions
import preprocessor as p
import helper

st.sidebar.title("WhatsApp Chat Analyser")

# insert file uploader to upload the chat file
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt"]) 
if uploaded_file is not None:
    # read the file
    data = uploaded_file.read().decode("utf-8")

    df = p.preprocess_chat_data(data)
    st.dataframe(df,use_container_width=True)

    # fetch unique users name
    df['user'] = df['user'].astype(str).str.strip()
    user_list = df['user'].unique().tolist()
    user_list.remove('group notification')
    user_list.sort()
    user_list.insert(0,'Overall')
    selected_user = st.sidebar.selectbox("Select user",user_list)

    if st.sidebar.button("show Analysis"):
        num_messages = helper.fetch_stats(selected_user,df)
        col1,col2,col3,col3 = st.columns(4) # split the page into 4 columns
        with col1:
            st.header("Total Meessages")
            st.title(num_messages)
