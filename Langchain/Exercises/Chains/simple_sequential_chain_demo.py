from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.globals import set_debug
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os

# Load env
load_dotenv()

#Set Debug
set_debug(True)

OPEN_API_KEY = os.getenv('OPEN_API_KEY')
# Prompt Template for Cuisine Exploration for a given country

title_prompt_template = PromptTemplate(
    input_variables=["topic"],
    template=""" 
       You are an experienced speech writer. You need to craft an impactful title for a speech on the
       following topic: {topic}
       Answer exactly with one title.
    """
)

speech_prompt_template = PromptTemplate(
    input_variables=["title"],
    template=""" 
       You need to write a powerful speech of 350 words for the following title: {title}
    """
)

llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

first_chain = title_prompt_template | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
second_chain = speech_prompt_template | llm
final_chain = first_chain | second_chain

# UI for Chat
st.title("Speech Generator")
topic = st.text_input("Enter your topic:")

if topic:
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)
