def fetch_stats(selected_user,df):
    selected_user = str(selected_user).strip()
    if selected_user == 'Overall':
        return df.shape[0]
    else:
        return df[df['user'].astype(str).str.strip()==selected_user].shape[0]