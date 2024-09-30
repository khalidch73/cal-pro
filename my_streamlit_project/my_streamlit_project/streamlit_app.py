# prompt: create upper code for streamlit

import streamlit as st

st.title("Calculator")

number1 = st.number_input("Number 1", value=100)
number2 = st.number_input("Number 2", value=100)

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
  result = number1 + number2
elif operation == "Subtract":
  result = number1 - number2
elif operation == "Multiply":
  result = number1 * number2
elif operation == "Divide":
  if number2 == 0:
    result = "Cannot divide by zero"
  else:
    result = number1 / number2

st.write(f"Result: {result}")
