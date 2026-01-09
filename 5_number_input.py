import streamlit as st
st.title("Number Input")

age = st.number_input("Enter your age:",min_value=0,max_value=80,value=25)

rating= st.slider("Give Rating:",min_value=0,max_value=10,step=2,value=2)
st.write(age)
