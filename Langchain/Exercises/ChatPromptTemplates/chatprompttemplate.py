from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.globals import set_debug
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

#Set Debug
set_debug(True)

OPEN_API_KEY = os.getenv('OPEN_API_KEY')
# Prompt Template for Cuisine Exploration for a given country

prompt_template = ChatPromptTemplate(
   [
       ("system", "You are a Agile coach. Answer any questions related to the agile process"),
       ("human", "{input}")
   ]
)

# UI for Chat
st.title("Agile Coach")

input = st.text_input("Enter your question")


llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

# LCEL usage chain

chain = prompt_template | llm

if input:
    response = chain.invoke({"input": input })
    st.write(response.content)
