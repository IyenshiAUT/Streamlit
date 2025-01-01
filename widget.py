import streamlit as st

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello {name}")
    
age = st.slider("Select your age ", 0, 100, 25)

st.write(f"Your age: {age}")


options = ["Pyhton", "C", "C++", "Java"]
choice = st.selectbox("Choose the preferred language", options)
st.write(f"You selected {choice}")