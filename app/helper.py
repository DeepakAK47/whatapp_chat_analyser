from turtle import pd

from wordcloud import WordCloud

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

# fetch most busy users in the group
def most_busy_users(df):
    # Top 5 most active users
    top_users = df['user'].value_counts().head(5)
    top_users.columns = ['user', 'count']
    
    # Percentage contribution of each user
    user_percentages = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
    user_percentages.columns = ['name', 'percentage']  # Proper naming
    
    return top_users, user_percentages 

# wordcloud generation
def create_wordcloud(selected_user, df):
    if selected_user == 'Overall':
        text = " ".join(df['message'].dropna().astype(str))
    else:
        text = " ".join(df[df['user'] == selected_user]['message'].dropna().astype(str))
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# most common words
