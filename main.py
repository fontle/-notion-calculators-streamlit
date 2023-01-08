import streamlit as st
import numpy as np 
st.title("Notion Calculators for Choice and Optimal Input Demands")


y = st.number_input("Output")
col1,col2 = st.columns(2)

a = col1.number_input("Good 1 preference", 0, 1)
b = col2.st.number_input("Good 2 preference", 0, 1)
e1 = col1.number_input("Endowment of good 1")
e2 = col2.number_input("Endowment of good 2")
alpha = st.slider("Preference factor (Alpha)", 0, 1)

st.latex("q_1^*=\cfrac{a(p_1e_1+p_2e_2)}{p_1}")

f"Optimal q1: {(a*(p1*e1+e2*p2))/p1}"
f"Optimal q2: {((1-a)(p1*e2+p2*e2))/p2}"
