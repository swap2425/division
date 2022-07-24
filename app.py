import streamlit as st


st.write("""
# Division of Two numbers

This app divides two numbers
""")
#Get Input

st.header('User Input Parameters')

num1=st.number_input("Enter one number")
num2=st.number_input("Enter another number")
if num2==0:
  st.write('Division by Zero not possible')
else:
  res=num1/num2

  st.subheader('Answer')

  st.write(res)

