import streamlit as st
from importlib.machinery import SourceFileLoader

# Aplikasi Streamlit
st.title("Denjaura Project")

# Input File or link 
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

input_file = SourceFileLoader('input_file' , 'dashboard/input_file_container/input_file.py').load_module()
input_file.test()
