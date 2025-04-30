import streamlit as st

st.title("Counter and re Run")
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1
    st.rerun()  # This will rerun the script from the top, which will reset the count to 0  

st.write(f"Count : {st.session_state.count}")
if st.button("Increment"):
    increment()

st.divider()
st.title("My app")

@st.fragment()
def toggle_and_run():
    col = st.columns(2)
    col[0] = st.toggle("Switch")
    col[1] = st.text_area("Enter Description")

@st.fragment()
def filter_and_file():
    cols = st.columns(15)
    cols[0] = st.checkbox("Checkbox")
    cols[1] = st.file_uploader("Upload Secret File")
    cols[2] = st.selectbox("Select Box", ["Option 1", "Option 2"])
    cols[3] = st.multiselect("Multi Select", ["Option 1", "Option 2"])
    cols[4] = st.camera_input("Camera Input")
    cols[5] =st.snow()
    cols[6] = st.progress(50, text="Progress")
    # add unique features of st in cols
    cols[7] = st.spinner("Loading...")
    cols[8] = st.balloons()
    cols[9] = st.metric("Metric", 100)
    cols[10] = st.chat_input("Chat Input")
    cols[11] = st.expander("Expander")
    cols[12] = st.echo("Echo")
    cols[13] = st.toast("Beware of my toast")

toggle_and_run()
filter_and_file()
# fragments are used to create reusable components in streamlit