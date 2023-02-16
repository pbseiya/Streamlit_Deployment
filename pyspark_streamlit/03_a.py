import pandas as pd
import streamlit as st
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

st.title('Recommendation System')

movies_path = 'https://raw.githubusercontent.com/smanihwr/ml-latest-small/master/movies.csv'
df_movies = pd.read_csv(movies_path)
df_movies['genres'] = df_movies['genres'].str.split('|')
mlb = MultiLabelBinarizer()
df_movies = pd.DataFrame(mlb.fit_transform(df_movies['genres']),
                        columns=mlb.classes_,
                        index=df_movies['title'])
df_movies = df_movies.iloc[:,1:]

for genre in df_movies.columns:
    st.sidebar.slider(genre, 0, 5)