import streamlit as st
st.title("Text Input")
name = st.text_input("Enter your Name:")
comments = st.text_area("Any Comments/Feedback:")

st.write("Live Output:")
if name:
    st.write(f"Hello {name}")
if comments:
    st.write("Your Comments:")
    st.write(comments)
