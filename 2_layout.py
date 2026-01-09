import streamlit as st
st.set_page_config(page_title="Hello Layout",page_icon="µ",layout='wide')
st.title("Faculty Profile")
st.sidebar.header("Profile Settings")
faculty = st.sidebar.text_input("Faculty Name","Tejas Thakkar")
department = st.sidebar.selectbox(" Department",['CE','CSE','IT','AIML'])
exp = st.sidebar.slider('Years of Experience',0,40,10)
st.sidebar.markdown("---")
col1,col2 = st.columns([1,2])
with col1:
    st.write("Basic Information")
    st.write(f"**Name:** {faculty}")
    st.write(f"**Department:** {department}")
    st.write(f"**Experience:** {exp}")
    
with col2:
    st.subheader("About")
    st.markdown("..............")

with st.expander("Subjects Taught"):
    st.write(" --CN")
    st.write(" --Python")
    st.write(" --SA-1")
    
