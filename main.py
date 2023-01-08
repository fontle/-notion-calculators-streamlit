import streamlit as st
import numpy as np 
st.title("Cobb-Douglas Gross Demand Calculator")

col1,col2 = st.columns(2)
p1= col1.number_input("Price of good 1", 0.01)
p2 = col2.number_input("Price of good 2", 0.01)
e1 = col1.number_input("Endowment of good 1")
e2 = col2.number_input("Endowment of good 2")
a = st.slider("Preference factor (a)", 0, 1, 0.01)

col1,col2 = st.columns(2)
col1.latex("q_1^*=\cfrac{a(p_1e_1+p_2e_2)}{p_1}")
col2.write(f"Optimal $q_1$: {(a*(p1*e1+e2*p2))/p1}")
col2.write(f"Optimal $q_2$: {((1-a)*(p1*e1+p2*e2))/p2}")
