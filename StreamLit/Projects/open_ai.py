import openai
import requests
from io import BytesIO
from PIL import Image
import streamlit as st

st.title("Prompt to Image Generation")
st.text("Please enter your OpenAI API key below:")
api_key = st.text_input("OpenAI API Key", type="password")
if api_key:
    openai.api_key = api_key
    st.success("API key set successfully!")

prompt = st.text_input("Enter your prompt here:")
if st.button('Generate'):
    if prompt:
        try:
            responce = openai.Image.create( prompt = prompt, n=1, size ='1024x1024')
            image_url = responce['data'][0]['url']

            responce = requests.get(image_url)
            img = Image.open(BytesIO(responce.content))
            st.image(img, caption='Generated Image', use_column_width=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.stop()


    else:
        st.error("Please enter a prompt to generate an image.")