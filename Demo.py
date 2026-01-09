import streamlit as st
import numpy as np
import datetime as dt
import time
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Streamlit Demo",
    page_icon='',
    layout="wide"
)

st.sidebar.title('Streamlit Topics')
page = st.sidebar.radio(
    'Go to Section', 
    ['UI & Layout',
     'Input Widgets',
     'Data Display',
     'Buttons & Files',
     'Media & Status',
     'Charts & Visualization',
     'BMI Calculator'])

if page == 'UI & Layout':
    st.title("UI Creation and Layout")
    st.header("Text Elements")
    st.subheader("Subheader Example")
    st.text("This is text")
    st.write("It can show text, numbers, tables,etc.")
    st.markdown("**Markdown** supports _formatting_")

    code = '''
    def add(a,b):
        return a+b
    print(add(3,7))'''

    st.code(code, language='python')
    st.divider()

    st.header("Columns & Expander")
    col1, col2 = st.columns(2)
    with col1:
        st.success("Column 1 content")
    with col2:
        st.info("Column 2 Content")

    with st.expander("Click to Expand"):
        st.write("Hidden Content Shown Here")

elif page == 'Input Widgets':
    st.title("Input Widgets and Interactivity")
    name = st.text_input('Enter Name')
    feedback = st.text_area("Enter Feedback")
    age = st.number_input('Age',1,100,18)
    rating = st.slider("Rate Session",1,10,5)

    course = st.selectbox('Select Course',['FSD-1','Python-1','PS','DE'])
    days = st.multiselect('Preferred Days',['Mon','Tue','Wed','Thu','Fri'])
    mode = st.radio('Mode',['Offline','Online'])
    subscribe = st.checkbox('Subscribe')
    exam_date = st.date_input("Exam Date",dt.date.today())
    exam_time = st.time_input("Exam Time",dt.time(9,0))

    st.markdown("### Live Output")
    st.write(f'Name: {name}')
    st.write(f'Age: {age}')
    st.write(f'Course: {course}')
    st.write(f'Days: {days}')
    st.write(f'Mode: {mode}')
    st.write(f'Subscribed: {subscribe}')
    st.write(f'Date: {exam_date}')
    st.write(f'Time: {exam_time}')

elif page == 'Data Display':
    st.title("Displaying Data")
    data = {
        "Student":['A','B','C'],
        "Marks":[85,90,34],
        "Pass": [True,True,False]
    }
    df = pd.DataFrame(data)

    st.subheader("DataFrame")
    st.dataframe(df)

    st.subheader("Table")
    st.table(df)

    st.subheader("JSON")
    st.json(data)

elif page == "Buttons & Files":
    st.title("Buttons, File Upload & Download")

    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    
    if st.button("Generate Sample Data"):
        df = pd.DataFrame({
            "Student":['A','B','C'],
            "Marks" : [86,56,34]
        })
        st.table(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            'Download CSV',
            csv,
            'marks.csv'
        )
elif page=="Media & Status":
    st.title("Media & Status Elements")
    st.success("Operation Successfull")
    st.info("This is some information")
    st.warning("This is a warning")
    st.error("This is an error message")
    if st.button("Start Task"):
        progress=st.progress(0)
        with st.spinner("Processing........"):
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i+1)
        st.success("Task Completed")
    st.subheader("Media Display")
    st.image("OIP.jpeg",width='content')
    st.image("https://picsum.photos/300/600",width='content')
    st.audio('sampleaudio.mp3')
    st.video('samplevideo.mp4')
    
elif page =="Charts & Visualization":
    st.title("Charts & Visualization")
    x=np.arange(1,101)
    y=np.random.randint(1,101,100)
    
    st.subheader("Matplotlib Line Chart")
    plt.figure()
    plt.plot(x,y,marker="*")
    plt.title("Random Line chart")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    st.pyplot(plt)
    st.subheader("Matplotlib Scatter plot")
    plt.figure()
    plt.scatter(x,y,marker='o')
    plt.title("Random Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    st.pyplot(plt)
    
    st.subheader("Streamlit Built-in Line Chart")
    data={
        'x':x,
        'y':y
    }
    df=pd.DataFrame(data)
    st.line_chart(df['y'])
    st.bar_chart(df['y'])
    st.area_chart(df['y'])
elif page == "BMI Calculator":
    st.title("BMI Calculator")
    st.write("Calculate your BMI and understand your weight category")
    weight = st.number_input('Weight(In kg)',1,200,40)
    height = st.number_input('Height(In cm)',1,500,200)
    if st.button("Calculate BMI"):
        if height<=0 or weight<=0:
            st.error("Height and weight must be greater than zero")
        else:
            height_m=height/100
            bmi=weight/(height/100)**2
            bmi=round(bmi,2)
            st.success(f"Your BMI is:{bmi}")
            if bmi<18:
                st.warning("Underweight")
            elif 18<=bmi<24:
                st.success("Normal Weight")
            elif 24<=bmi<30:
                st.warning("Overweight")
            else:
                st.error("Obesity")
    
    
    
        
     
    
    
    
    
    
    
    
    
    
        
    