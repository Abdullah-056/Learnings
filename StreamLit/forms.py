import streamlit as st
from datetime import datetime

min_date = datetime(1990, 1, 1)
max_date = datetime.today()

st.title("User Information")
form_values = {}
with st.form(key = 'user_info_form'):
    form_values['name'] = st.text_input("Enter Your Name: ")
    form_values['height'] = st.number_input("Enter your Height: ")
    form_values['gender'] = st.selectbox("Gender",['Male','Female'])
    form_values['DOB'] = st.date_input("Enter your Birthday Date  ", max_value=max_date, min_value=min_date)

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if not all(form_values.values()):
        st.warning("Please fill all the fields")
    else:
        st.balloons()
        st.write("### Info ")
        for (key, value) in form_values.items():
            st.write(f"{key}: {value}")

