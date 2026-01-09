from datetime import date,time
import streamlit as st

st.title('Date, Time & File ')
exam_date = st.date_input("Select Exam Date",value=date.today())
start_time = st.time_input("Exam Start Time",value=time(14,0))

file = st.file_uploader("Upload your CSV File:",type=['csv'])
st.write(f"Exam Date: {exam_date}")
st.write(f"Start Time: {start_time}")
