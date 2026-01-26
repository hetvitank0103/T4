import streamlit as st
from datetime import date
st.set_page_config(page_title="Hello Notice Board",page_icon="µ",layout='wide')

st.title("Notice Board")
st.sidebar.header("Filter Notices")
selected = st.sidebar.selectbox("Notice Category", ['All',"Exams","Workshops","Internships",'General'])
show_past = st.sidebar.checkbox("Show Past Notices",value=True)
notices=[
    {'title':'T1 Exam Schedule','category':'Exams','date':date(2025,3,10)},
    {'title':'Python Workshop','category':'Workshops','date':date(2025,11,18)},
    {'title':'Internship Orientation','category':'Internships','date':date(2025,3,10)},
    {'title':'Parent- Teacher Meeting','category':'General','date':date(2025,3,10)},    
]

st.header("Notices")
col1,col2 = st.columns([1,2])

with col1:
    st.subheader("Filter Applied")
    st.write(f"Category: **{selected}**")
    st.write(f"Include Past Notices: {show_past}")
with col2:
    st.subheader("Information")
    st.text("Below are the notices after filtering")

for notice in notices:
    if selected != 'All' and notice['category'] != selected:
        continue
    with st.expander(f"{notice['title']} {(notice['category'])}"):
        st.write(f"**Date** {notice['date']}")
        st.write("Notice Details.....")
