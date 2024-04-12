# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


KEY = os.getenv("OPENAI_API_KEY")


def get_responses(input):
    llm = OpenAI(openai_api_key=KEY,temperature=0.6,model_name="gpt-3.5-turbo-instruct")
    response = llm(input)
    return response



##initialize our streamlit app

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_responses(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)



