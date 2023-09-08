import streamlit as st
import pandas as pd

# Create a title and description
st.title("CSV File Column Data Types Checker")
st.write("Upload a CSV file to check the data types of its columns.")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display DataFrame
    st.write("Preview of the uploaded data:")
    st.write(df.head())

    # Get column data types
    data_types = df.dtypes

    # Display column data types
    st.write("Data types of columns:")
    st.write(data_types)
