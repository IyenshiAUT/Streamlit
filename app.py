import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("Hello Streamlit")

# a simple text 
st.write("This is a simple text")

df = pd.DataFrame({
    "column_1": [1, 2, 3, 4, 5],
    "column_2": [2, 4, 6, 8, 10]
})

# create a simple dataframe
st.write("Here is the dataframe")
st.write(df)

chart_Data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.line_chart(chart_Data)
