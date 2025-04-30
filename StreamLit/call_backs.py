import streamlit as st

if 'step' not in st.session_state:
    st.session_state.step = 1

if 'info' not in st.session_state:
    st.session_state.info = {}

def go_to_step2(name):
    st.session_state.info['name'] = name
    st.session_state.step = 2

if st.session_state.step == 1:
    st.title("Part 1: Information")
    name = st.text_input("Name: ", value=st.session_state.info.get('name', ''))
    st.button("Next", on_click=go_to_step2, args=(name,))

def go_to_step1():
    st.session_state.step = 1
    st.session_state.info = {}

if st.session_state.step == 2:
    st.title("Part 2: Information Display")
    st.write(f"Name: {st.session_state.info.get('name', '')}")

    if st.button('Submit'):
        st.write("Success")
        st.balloons()
        st.session_state.info = {}

    st.button("Back", on_click=go_to_step1)