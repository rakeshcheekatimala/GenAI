import os
from langchain_openai import ChatOpenAI
from langchain.prompts import  PromptTemplate
import  Langchain.Exercises.StreamlitDemos.streamlit as st
from dotenv import load_dotenv
# Load env
load_dotenv()
OPEN_API_KEY = os.getenv('OPEN_API_KEY')

# Title of Streamlit App
st.title("Interview Tips Generator")

# UI Components
company = st.text_input("Company Name")
position = st.text_input("Position Title")
strengths = st.text_area("Your Strengths")
weakness = st.text_area("Your Weakness")

# Prompt Template

prompt_template = PromptTemplate(
    input_variables = ["company", "position", "strengths", "weakness"],
    template = """
        You are career coach. Provide tailored interview tips for the position of {position} at {company}.
        Highlight your strengths in {strengths} and prepare for questions about your weakness such as {weakness}.
    """
)

# LLM

llm = ChatOpenAI(model='gpt-4o', api_key=OPEN_API_KEY)

if company and position and strengths and weakness:
    response = llm.invoke(prompt_template.format(company=company, position = position , strengths = strengths , weakness = weakness))
    st.write(response.content)
