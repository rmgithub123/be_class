import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
y2 = np.array([1, 3, 5, 7, 9])

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the first line
ax.plot(x, y1, label='Line 1')

# Plot the second line
ax.plot(x, y2, label='Line 2')

# Add a title and labels to the axes
ax.set_title('Two Line Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a legend
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)
