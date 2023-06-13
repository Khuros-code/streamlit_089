import streamlit as st
import numpy as np
raw_data = st.text_input('Enter the Data', value = 0)
raw_data = raw_data.strip()
data = raw_data.replace(" , ", " ").replace(", ", " ").replace(" ,", " ").replace(" ", ',').split(',')
x = [float(i) for i in data]
mu = st.text_input('Enter Population Mean', value = 0)
mu = float(mu)
xbar = np.mean(x)
sigma = np.std(x, ddof = 1)
n = len(x)
z_cal = (xbar - mu) / (sigma / np.sqrt(n))
st.write("Your z - statistic value is: ", np.round(z_cal, 3))