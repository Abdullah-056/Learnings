import streamlit as st
import pandas as pd
st.write("Hello World 123")     # Used to write on page 
3 * 8       # It can also work
# It always runs whole code every time
pressed = st.button("Press Me")
print(pressed)

st.title("Simplest Title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("- This is a *markdown*")
st.caption("This is a caption")
st.divider()
code_example = '''
def greet(name):
    return f"Hello, {name}!"
'''
st.code(code_example, language='python')
st.divider()
import os
st.image(os.getcwd() + './static/sample.jpeg',width=500, caption="Sample Image")
st.divider()


# creating a dataframe of 5 rows and 5 columns
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E'],
    'Column 3': [True, False, True, False, True],
    'Column 4': [1.1, 2.2, 3.3, 4.4, 5.5],
    'Column 5': pd.date_range('20230101', periods=5)
})
st.dataframe(df)

# Editable dataframe
st.subheader("Editable DataFrame")
editable_df = st.data_editor(df)
# Print this to get updated data

st.subheader("Static Table")
st.table(df)    # If we donot want properties like editibility
# , sort and filter

# Metrics
st.subheader("Metrics")
st.metric(label='Total Rows', value=len(df))
st.metric(label='Total Columns', value=len(df.columns))

st.subheader("JSON and Dictationary")
data = {
    "Name":['Abdullah',"Ali"],
    'age':[23,24],
    'skills':['Python', 'Java'],
}
st.json(data)
st.write("dictationary Values: ",data)