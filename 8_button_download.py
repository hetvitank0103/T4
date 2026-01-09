import streamlit as st
import pandas as pd

if st.button("Click to Generate Marks"):
    df=pd.DataFrame({
        'Roll No':[1,2,3,4,5],'Marks':[78,85,74,89,52]
    })
    st.write('Generated Data')
    st.dataframe(df)
    csv=df.to_csv(index=False,encoding='utf-8')
    st.download_button(label='Download as CSV',data=csv,file_name='marks.csv',mime='text/csv')
