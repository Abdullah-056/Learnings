import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd

st.title("Charts Demo")
chart_data = pd.DataFrame({
    # Create a DataFrame with random data
    'a':[2,9,5,1],
    'b':[4,3,2,5],
    'c':[1,9,3,4],
})
st.subheader("Area chart")
st.area_chart(chart_data)

st.subheader("Scatter Plot")
scat = pd.DataFrame({
    'x':[1,2,3,4, 8, 2,1,9,3,4],
    'y':[4,3,2,1, 1, 9,3,4,2,5],
})
st.scatter_chart(scat)
st.divider()

# Showing points on a map
st.subheader("Map")
map_data = pd.DataFrame({
    'lat':[37.76, 37.77, 37.78, 37.79],
    'lon':[122.41, 122.42, 122.43, 122.44],
})
st.map(map_data, zoom=12)  # Added zoom parameter for better visibility
st.divider()

st.subheader('Pyplot')
import matplotlib.pyplot as plt
import numpy as np
# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

st.pyplot(fig)