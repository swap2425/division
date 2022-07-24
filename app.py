import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle

st.write("""
# Division of Two numbers

This app divides two numbers
""")
#Get Input

st.header('User Input Parameters')

num1=st.number_input("Enter onr number")
num2=st.number_input("Enter another number")

res=num1/num2

st.subheader('Answer')

st.write(res)
