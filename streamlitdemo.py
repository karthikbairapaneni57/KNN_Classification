import streamlit as st
st.title("my first streamlit app")
st.write("Hello,streamlit")
name=st.text_input("Enter your name")
if name:
    st.success(f"hello,{name}")

st.title("karthik")