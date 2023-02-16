import pandas as pd
import streamlit as st
from sklearn.svm import SVC
import numpy as np

if 'clf' not in st.session_state:
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    st.session_state['clf'] = SVC()
    st.session_state['clf'].fit(df.iloc[:,:4], df.iloc[:,-1])

attrs = ['sepal length (cm)',
         'sepal width (cm)',
         'petal length (cm)',
         'petal_width (cm)']
st.title('Iris Classification')
x = []
for attr in attrs:
    x.append(st.sidebar.number_input(attr))
x = np.array(x)

if st.sidebar.button('predict'):
    y = st.session_state['clf'].predict(x[None,:])
    st.text(f'Predict: {y[0]}')
