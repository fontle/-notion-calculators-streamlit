import streamlit as st
import numpy as np 
st.title("Choice and Optimal Demand Calculators")

st.header("Choice with Cobb-Douglas")
col1,col2 = st.columns(2)
p1= col1.number_input("Price of good 1", 0.01)
p2 = col2.number_input("Price of good 2", 0.01)
e1 = col1.number_input("Endowment of good 1", value=1)
e2 = col2.number_input("Endowment of good 2", value=1)
a = st.number_input("Preference factor (a)", 0.0, 1.0, value=0.5, step=0.01)

col1,col2 = st.columns(2)
col1.latex("q_1^*=\cfrac{a(p_1e_1+p_2e_2)}{p_1}")
col2.latex("q_1^*=\cfrac{(1-a)(p_1e_1+p_2e_2)}{p_2}")
""
col1.write(f"Optimal $q_1$: {(a*(p1*e1+e2*p2))/p1}")
col2.write(f"Optimal $q_2$: {((1-a)*(p1*e1+p2*e2))/p2}")

st.subheader("With Money Income") 
m = st.number_input("Money", value=0)

col1,col2 = st.columns(2)
col1.latex("q_1^*=\cfrac{am}{p_1}")
col2.latex("q^*_2=\cfrac{(1-a)m}{p_2}")
col1.write(f"Optimal $q_1$: {(a*m)/p1}")
col2.write(f"Optimal $q_2$: {((1-a)*m)/p2}")
