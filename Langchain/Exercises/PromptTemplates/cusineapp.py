from langchain_community.chat_models import ChatOllama
import Langchain.Exercises.StreamlitDemos.streamlit as st
from langchain.prompts import  PromptTemplate
from langchain.globals import set_debug

#Set Debug
set_debug(True)

# Prompt Template for Cuisine Exploration for a given country

prompt_template = PromptTemplate(
    input_variables = ['country','no_of_paras','language'],
    template="""
        You are expert in traditional cuisines. You provide information about specific 
        dish from the specific country. 
        Avoid giving information about fictional places. If the country is fictional or non-existent answer: I don't know. 
        Answer: What is the traditional cuisine of the country {country}?
        Answer in {no_of_paras} short paras in {language}
    """
)

# UI for Chat
st.title("Cuisine Info")

country = st.text_input("Please enter your country here")
language = st.text_input("Enter your language here")
no_of_paras = st.number_input("Input Number",min_value=1,max_value=5)

llm = ChatOllama(model="mistral:latest")

if country:
    response = llm.invoke(prompt_template.format(country=country,no_of_paras=no_of_paras,language=language))
    st.write(response.content)