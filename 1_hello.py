import streamlit as st
st.set_page_config(page_title="Hello Streamlit",page_icon="¥",layout='centered')
st.title("Welcome to Streamlit")
st.header("This is Header")
st.subheader("This is SubHeader")
st.text('This is _st.text()_')
st.write("This is **_st.write()_**")
st.markdown("This is _Markdown_")
code = """
def add(a,b):
    return a+b
result = add(3,5)
print(result)
"""
st.code(code,language='python')
st.code(code,language='C')
