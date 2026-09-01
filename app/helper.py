def fetch_stats(selected_user,df):
    selected_user = str(selected_user).strip()
    if df.empty:
        return 0,0,0
    elif selected_user == 'Overall':
        # 1. feching total number of messages
        num_messages = df.shape[0]
        # number of word
        words = []
        for message in df['message']:
            words.extend(message.split())
        # fetching total number of media messages
        media_messages = df[df['message'] == '<Media omitted>'].shape[0]
        return num_messages,len(words),media_messages
    else:
        #1. feching total number of messages
        new_df = df[df['user']==selected_user]
        num_messages = new_df.shape[0]
        words = []
        for message in new_df['message']:
            words.extend(message.split())
        #2. fetching total number of media messages
        media_messages = new_df[new_df['message'] == '<Media omitted>'].shape[0]    
        return num_messages,len(words),media_messages   