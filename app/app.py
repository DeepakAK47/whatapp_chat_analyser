import streamlit as st
import pandas as pd
import numpy as np
import re # it gives access to regex functions
import preprocessor as p
import helper
import matplotlib.pyplot as plt

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
        st.write(f"Analysis of {selected_user} is shown below ")

        # stat Area
        try:
            num_messages,words,media_messages = helper.fetch_stats(selected_user,df)
            col1,col2,col3 = st.columns([3,3,3]) # split the page into 3 columns
            with col1:
                st.header("Total Meessages")
                st.title(num_messages)
            with col2:
                st.header("total words")
                st.title(words)
            with col3:
                st.header("Media Messages")
                st.title(media_messages)   
        except Exception as e:
            st.error(f"error : {e}")
            st.stop()


        # finding the bussiest user in the group (if selected user is overall)
        if selected_user == 'Overall':
            try:
                x,new_df = helper.most_busy_users(df)
                st.title("Most Busy Users")
                col1,col2 = st.columns([3,3])
                with col1:
                    st.dataframe(x,use_container_width=True)
                with col2:
                    st.dataframe(new_df,use_container_width=True)
            except Exception as e:
                st.error(f"error : {e}")
                st.stop()

        # wordcloud generation
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')

        st.title('Most commmon words')
        st.pyplot(fig)      