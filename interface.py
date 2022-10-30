from attr import NOTHING
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt
from csv_processor import *
from io import StringIO


def get_file():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.session_state.uploaded_file = stringio
        st.session_state.csv_data = read_file(stringio)
        st.session_state.column_list = get_column_list(st.session_state.csv_data)
        return stringio
    else:
        return None


def set_csv_data(data):
    st.session_state.csv_data = data


def set_column_list(data):
    st.session_state.column_list = data


def plot_graph(selected_plot):
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(10, 6))
    try:
        if selected_plot == "Line":
            st.line_chart(
                x=st.session_state.x_axis,
                y=st.session_state.y_axis,
                data=st.session_state.csv_data,
            )
        elif selected_plot == "Bar":
            st.bar_chart(
                x=st.session_state.x_axis,
                y=st.session_state.y_axis,
                data=st.session_state.csv_data,
            )
        elif selected_plot == "Histogram":
            sb.histplot(x=st.session_state.x_axis, data=st.session_state.csv_data)
            st.pyplot(fig)
        else:
            return
    except Exception as e:
        st.text("Error: Please select a valid column for the corresponding plot type!")
        st.text(str(e))


def interface_main():
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None

    if "column_list" not in st.session_state:
        st.session_state.column_list = []

    if "csv_data" not in st.session_state:
        st.session_state.csv_data = None

    if "plot_type" not in st.session_state:
        st.session_state.plot_type = "Line"

    st.title("CSV Analyzer")
    get_file()
    st.selectbox(label="X Axis:", options=st.session_state.column_list, key="x_axis")
    st.selectbox(
        label="Y Axis:",
        options=st.session_state.column_list,
        key="y_axis",
        disabled=(st.session_state.plot_type == "Histogram"),
    )
    st.selectbox(
        label="Plot type:",
        options=["Line", "Bar", "Histogram"],
        key="plot_type",
        disabled=(st.session_state.uploaded_file is None),
    )
    if st.session_state.csv_data is not None:
        selected_plot = st.session_state.plot_type
        plot_graph(selected_plot)
