import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Student Marks & Feedback Form", page_icon="📝", layout="centered")

st.title("📝 Student Marks & Feedback Form")

st.header("1. Student Information")

col1, col2 = st.columns(2)

with col1:
    enrollment = st.text_input("Enrollment Number")
    name = st.text_input("Student Name")

with col2:
    semester = st.selectbox("Semester", ["3", "4", "5", "6", "7", "8"])
    division = st.text_input("Division", "CSE-A")

exam_date = st.date_input("Exam Date", value=date.today())

st.header("2. Marks Entry")

marks_py1 = st.number_input("Python-1 Marks (out of 100)", min_value=0, max_value=100, value=0)
marks_fsd1 = st.number_input("FSD-1 Marks (out of 100)", min_value=0, max_value=100, value=0)
marks_de = st.number_input("DE Marks (out of 100)", min_value=0, max_value=100, value=0)

st.header("3. Feedback")

understanding = st.slider("How well did you understand the subject?", 1, 10, 7)
participation = st.radio("Class Participation", ["Low", "Medium", "High"])
comments = st.text_area("Additional Comments")

if st.button("Submit Record"):
    if not enrollment or not name:
        st.error("Please fill Enrollment Number and Student Name.")
    else:
        df = pd.DataFrame({
            "Enrollment": [enrollment],
            "Name": [name],
            "Semester": [semester],
            "Division": [division],
            "Exam Date": [exam_date],
            "Python-1": [marks_py1],
            "FSD-1": [marks_fsd1],
            "DE": [marks_de],
            "Understanding (1–10)": [understanding],
            "Participation": [participation],
            "Comments": [comments]
        })

        st.success("Record submitted successfully!")
        st.subheader("Preview of Submitted Data")
        st.dataframe(df)

        csv = df.to_csv(index=False , encoding ="utf-8")
        st.download_button(
            label="Download this record as CSV",
            data=csv,
            file_name=f"{enrollment}_record.csv",
            mime="text/csv"
        )
