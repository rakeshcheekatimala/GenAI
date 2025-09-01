from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import  PromptTemplate
from langchain.globals import set_debug
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

#Set Debug
set_debug(True)

OPEN_API_KEY = os.getenv('OPEN_API_KEY')
# Prompt Template for Cuisine Exploration for a given country

prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template=""" 
        Welcome to the {city} travel guide!
        If you're visiting in {month}, here's what you can do:
        1. Must-visit attractions. 
        2. Local cuisine you must try.
        3. Useful phrases in {language}
        4. Tips for travelling on a {budget} budget.
        Enjoy your trip!
    """
)

# UI for Chat
st.title("Travel Guide")

city = st.text_input("Enter the city:")
month = st.text_input("Enter Month of travel:")
language = st.text_input("Enter your language:")
budget = st.selectbox("Travel Budget",["Low","Medium","High"])

llm = ChatOpenAI(model="gpt-4o",api_key=OPEN_API_KEY)

if city and month and language and budget:
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)