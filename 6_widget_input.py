import streamlit as st

course = st.selectbox("Select Course",['Python','FSD','DE','PS'])
preferred_days = st.multiselect("Preferred days for Extra Lectures:", ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
lec_no = st.radio("Preferred Lec No:",[1,2,3,4])

st.write(f"Preferred Days: {','.join(preferred_days) if preferred_days else 'None'}")
