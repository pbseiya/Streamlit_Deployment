import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.title('My data visualization')
ds = st.selectbox("Choose a dataset", sns.get_dataset_names())
# st.write(ds)
df = sns.load_dataset(ds)
st.write(df)

corr = df.corr()
fig = plt.figure()
sns.heatmap(corr, annot=corr)
st.write(fig)