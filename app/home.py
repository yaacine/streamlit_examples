import streamlit as st
import pandas as pd

st.header("Home")



st.subheader("This is a subheader")

df = pd.DataFrame({"sun":[1,2,3], "earch":[4,5,6], "march":[7,8,9]})
st.area_chart(df, width=0, height=0, use_container_width=True)