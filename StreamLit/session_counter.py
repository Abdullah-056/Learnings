import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented at {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
    st.write(f"Counter value is reseted to : {st.session_state.counter}")