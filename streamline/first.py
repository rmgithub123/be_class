import pandas as pd
import numpy as np
import streamlit as st
st.title("Simple Calculator")
st.write("Perform basic calculations with this interactive calculator!")
# ==========
num1 = st.number_input("Enter the first number:", step=0.1)
operation = st.selectbox("Select an operation:", ["+", "-", "*", "/"])
num2 = st.number_input("Enter the second number:", step=0.1)
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

st.write(f"Result: {result}")

