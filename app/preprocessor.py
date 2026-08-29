# it return the data in required format for further processing
import pandas as pd
import numpy as np
import re

def preprocess_chat_data(data):
    # pattern format
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)

    # Create a DataFrame from the extracted messages
    df = pd.DataFrame({'message_date': dates, 'user_message': messages})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')    

    # seperating user and message
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s',message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['message'], inplace=True)
    df.head(20)   

    # extracting the dates from the chat data
    df['year'] = df['message_date'].dt.year
    df['month'] = df['message_date'].dt.month_name()
    df['day'] = df['message_date'].dt.day  

    # extracting hours
    df['hour'] = df['message_date'].dt.hour
    #extracting minutes
    df['minute'] = df['message_date'].dt.minute
    # removing message_date column as we have extracted all the information from it
    df.drop(columns=['message_date'], inplace=True)
    return df
