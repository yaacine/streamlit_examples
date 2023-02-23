import streamlit as st

st.header("Page2")

my_image = st.camera_input("Take a picture", key="my_camera")

if my_image is not None:
    st.image(my_image, channels="BGR")