import streamlit as st
import interface

def get_file():
    uploaded_file = st.file_uploader('Choose a file')
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        return stringio
    else:
        return None

def set_csv_data(data):
    st.session_state.csv_data = data

def set_column_list(data):
    st.session_state.column_list = data

def interface_main():
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None

    if 'column_list' not in st.session_state:
       st.session_state.column_list = ['Age', 'Gender']
    
    
    if 'csv_data' not in st.session_state:
       st.session_state.csv_data = None
    
    st.title('CSV Analayzer')
    st.session_state.uploaded_file = get_file();
    st.selectbox(label='X Axis:', options=st.session_state.column_list, key='x_axis')
    st.selectbox(label='Y Axis:', options=st.session_state.column_list, key='y_axis')
    st.text("X Axis: "+st.session_state.x_axis)
    st.text("Y Axis: "+st.session_state.y_axis)
