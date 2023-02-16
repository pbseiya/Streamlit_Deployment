import streamlit as st
from pyspark.sql import SparkSession
import os
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier

os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jre1.8.0_361'
os.environ['PYSPARK_PYTHON'] = 'C:/Users/TON/miniconda3/python.exe'

schema = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
if 'clf' not in st.session_state:
    with st.spinner('Training ...'):
        st.session_state['spark'] = SparkSession.builder.appName('test').getOrCreate()

        df = st.session_state['spark'].read.csv('iris.csv', header=False, inferSchema=True)
        df = df.toDF(*schema)

        st.session_state['feature_assembler'] = VectorAssembler(inputCols=schema[:-1],
                                            outputCol='features')
        df = st.session_state['feature_assembler'].transform(df)
        indexer = StringIndexer(inputCol='species', outputCol='label')
        st.session_state['indexer'] = indexer.fit(df)
        df = st.session_state['indexer'].transform(df)

        rf = RandomForestClassifier(featuresCol='features', labelCol='label')
        st.session_state['clf'] = rf.fit(df)

sl = st.sidebar.text_input('sepal length in cm')
sw = st.sidebar.text_input('sepal width in cm')
pl = st.sidebar.text_input('petal length in cm')
pw = st.sidebar.text_input('petal width in cm')

if st.sidebar.button('Predict'):
    with st.spinner('Predicting...'):
        F = [(float(sl), float(sw), float(pl), float(pw))]
        df_test = st.session_state['spark'].createDataFrame(F, schema=schema[:-1])
        df_test = st.session_state['feature_assembler'].transform(df_test)
        df_test = st.session_state['clf'].transform(df_test)
        z = df_test.first()['prediction']
        z = st.session_state['indexer'].labels[int(z)]
        st.text(f'Predict: {z}')
