import pandas as pd
import streamlit as st
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

st.title('Recommendation System')

if 'df' not in st.session_state:
    movies_path = 'https://raw.githubusercontent.com/smanihwr/ml-latest-small/master/movies.csv'
    df_movies = pd.read_csv(movies_path)
    df_movies['genres'] = df_movies['genres'].str.split('|')
    mlb = MultiLabelBinarizer()
    df_movies = pd.DataFrame(mlb.fit_transform(df_movies['genres']),
                            columns=mlb.classes_,
                            index=df_movies['title'])
    st.session_state['df'] = df_movies.iloc[:,1:]

user_profile = []
for genre in st.session_state['df'].columns:
    user_profile.append(st.sidebar.slider(genre,0,5))
user_profile = np.array((user_profile))
sum_user_profile = user_profile.sum()
# if sum_user_profile > 0:
#     user_profile = user_profile / sum_user_profile
#     ranking = st.session_state['df'] @ user_profile
#     ranking = ranking.sort_values(ascending=False)
#     st.write(ranking)