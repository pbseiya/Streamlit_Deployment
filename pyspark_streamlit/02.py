import streamlit as st
import numpy as np
from PIL import Image, ImageColor
import pandas as pd

name = st.text_input('name')
age = st.number_input('age',step=1)
info = st.text_area('Tell us about you')
birthday = st.date_input('Birthday')
wakeup = st.time_input('Wake up')
photo = st.camera_input('Cheese!!')
if photo is not None:
    img = np.array(Image.open(photo).resize((200,150)))
    img = img[:,::-1,:]
    st.image(img)

df = pd.DataFrame(columns=['name','age','birthday','wakeup'])
df.loc[len(df)] = [name,age,birthday,wakeup]
st.download_button('Download data',
                   df.to_csv(index=False).encode(),'data.csv')

st.download_button('Download file', open('./pyspark_streamlit/01.py'), 'streamlit.py')
csv = st.file_uploader('Upload csv file')
if csv is not None:
    st.write(pd.read_csv(csv))

clicked = st.button('ok')
if clicked:
    st.text('clicked')

selected = st.checkbox('Agree')
if selected is not None:
    st.text('You agree')

st.image(np.full((100,100,3),[255,0,0]))
choice = st.radio('color?', ["don't know",'red','green','blue'])
if choice == 'red':
    st.text('red')
else:
    st.text('try again')

choices = st.multiselect('genres?',
                        ['Action', 'Romance','Horror','Sci-Fi'])
st.write(choices)

rating = st.slider('Rate this item',1,5)
st.text(rating)

color = st.color_picker('color?')
color = ImageColor.getcolor(color,'RGB')
st.write(color)