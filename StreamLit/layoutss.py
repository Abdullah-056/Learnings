import streamlit as st

st.sidebar.title("This is Sidebar")
st.sidebar.write("This is text in sidebar.")
sidebar_input = st.sidebar.text_input('Enter Something Here: ')
if sidebar_input:
    st.sidebar.write(f"thanks. The input is: {sidebar_input}")

# Create tabs 
tab1, tab2, tab3  = st.tabs(['Tab 1 ', 'Tab 2', 'Tab 3'])

with tab1:
    st.write("You are in Tab1")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Column1")
        st.write("Contents of Column 1 will go here")
    with col2:
        st.header("Column2")
        st.write("Contents of Column 2 will go here")

with tab2:
    st.write("You are in Tab2")
    # Container example
    with st.container(border=True):
        st.write("This is a container")
        st.write("You can add multiple elements here")

with tab3:
    st.write("You are in Tab3")

    # Empty PlaceHolder
    place = st.empty()
    place.write("This is an empty placeholder")
    if st.button("Update PlaceHolder"):
        place.write("This is an Updated PlaceHolder")


with st.expander("Expand for more details"):
    st.write("This is extra text that you can read now.")
    st.write("Click the arrow again to hide this text.")

st.write("hover over the button below:")
st.button("Button with tooltip", help='Be kind to Others')




