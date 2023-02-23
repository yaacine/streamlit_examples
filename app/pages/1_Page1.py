import streamlit as st
import requests as req
st.header("Page1")

with st.form(key="my_form"):
    name= st.text_input(label="Enter your name", value="Type Here")
    email= st.text_input(label="Enter your email", value="Type Here")
    submitted = st.form_submit_button(label="Submit")
    if submitted:
        st.write("name: ", name, "email: ", email)
        respone = req.get(f"https://api.agify.io?name={name}")
        st.json(respone.json())
