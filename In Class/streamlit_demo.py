'''
to run, put in terminal: streamlit run streamlit_demo.py

'''

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write("## [Streamlit Homepage](https://streamlit.io/gallery)")

st.sidebar.header("Parameters")
x = int(st.sidebar.text_input("Number of iterations"))
norms = np.random.randn(x)
fig, axes = plt.subplots(figsize = (4,2))
axes.hist(norms, bins = 50, edgecolor = "w")
st.pyplot(fig)


button = st.button("Click me!")

if button:
    st.header("Hello!")

