import streamlit as st
from pyspark.sql import SparkSession
import os

os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jre1.8.0_361'
os.environ['PYSPARK_PYTHON'] = 'C:/Users/TON/miniconda3/python.exe'


spark = SparkSession.builder.appName('test').getOrCreate()

df = spark.createDataFrame([(1, 'a'),
                           (2, 'b'),
                           (3, 'c')],
                          schema=['id', 'name'])

st.title('Spark')
st.write(df.toPandas())
