# it return the data in required format for further processing
import pandas as pd
import numpy as np
import re

def preprocess_chat_data(data):
    # pattern format
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)

    # Create a DataFrame from the extracted messages
    df = pd.DataFrame({'message_date': dates, 'user_message': messages})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')    

    # seperating user and message
    users = []
    messages = []
    for message in df['user_message']:
        msg = str(message).strip()
        if not msg:
            users.append("group_notification")
            messages.append('')
            continue
        if ':' in msg:
            user_part,msg_part = msg.split(':',1)
            users.append(user_part.strip())
            messages.append(msg_part.strip())
        else:
            users.append("group notification")
            messages.append(msg.strip())
    df['user'] = users        
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)  

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
