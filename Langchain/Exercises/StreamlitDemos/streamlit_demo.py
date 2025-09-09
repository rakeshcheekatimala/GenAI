from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain.globals import set_debug

# To add Debugging
set_debug(True)

# UI for Chat
st.title("Chat With Mistral Model")

question = st.text_input("Please enter your question here")

llm = ChatOllama(model="mistral:latest")

if question:
    response = llm.invoke(question)
    st.write(response.content)