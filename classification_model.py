import pandas as pd
import streamlit as st

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris_data = load_iris()
    df = pd.DataFrame(iris_data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    return df, iris_data.target_names 

df, target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])
