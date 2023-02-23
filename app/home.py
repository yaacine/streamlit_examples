import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import numpy as np

st.header("Home")



st.subheader("This is a subheader")

df = pd.DataFrame({"sun":[10,2,13], "earch":[14,55,6], "march":[70,81,92]})
st.area_chart(df, width=0, height=0, use_container_width=True)

st.bar_chart(df, width=0, height=0, use_container_width=True)



# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)