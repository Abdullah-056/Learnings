import streamlit as st
import time

# Cache is used to cache the results of a function so that it does not have to be
# recomputed every time it is called with the same arguments.

@st.cache_data(ttl=20)
def fetch_data():
    time.sleep(5)
    return {'data':'Data is returned from the server'}


# st.write(f"data is {fetch_data()}")
# st.write("Data is cached for 20 seconds")
# st.divider()

# instead of making files for multiple users, create one that everyone shares
file = 'example.txt'

@st.cache_resource
def get_file_handler():
    return open(file,'a+')

# Initialize file handler
if 'file_handler' not in st.session_state:
    st.session_state.file_handler = get_file_handler()

if st.button("write to the file"):
    st.session_state.file_handler.write("New Line of code\n")
    st.session_state.file_handler.flush() # this helps to write the data to the file
    st.success("Data written to the file")

if st.button("Read Data"):
    st.session_state.file_handler.seek(0)    # This helps to move the cursor to the start of the file
    data = st.session_state.file_handler.read()
    st.text(data)

if st.button("Clear"):
    st.session_state.file_handler.close()
    st.session_state.file_handler = get_file_handler()  # Reopen the file
    st.success("File cleared and reopened")

