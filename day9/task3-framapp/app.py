import streamlit as st

with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0)

    submit = st.form_submit_button("Submit")

if submit:
    if age <= 0:
        st.error("Age must be greater than 0")

    elif "@" not in email:
        st.error("Invalid email address")

    else:
        st.success("Form submitted successfully")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Age:", age)