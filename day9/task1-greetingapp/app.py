import streamlit as st

st.title("Welcome to Greeting App")

if "name" not in st.session_state:
    st.session_state["name"] = ""

name = st.text_input("Enter your name")

if st.button("Greet"):
    st.session_state["name"] = name

if st.session_state["name"]:
    st.write(f"Hello, {st.session_state['name']}!")