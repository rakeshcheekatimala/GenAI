import os
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Load env
load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# LLM
llm = ChatOpenAI(model="gpt-4o",api_key=OPEN_API_KEY)

# Chains
outline_prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="""
        You are a professional blogger.
        Create an outline for a blog post on the following topic: {topic}
        The outline should include:
        - Introduction
        - 3 main points with subpoints
        - Conclusion
    """
)

introduction_prompt = PromptTemplate(
    input_variable=['outline'],
    template="""
    You are a professional blogger.
    Write an engaging introduction paragraph based on the following
    outline:{outline}
    The introduction should hook the reader and provide a brief
    overview of the topic.
    """
)

first_chain = outline_prompt_template | llm | StrOutputParser()
final_chain = first_chain | introduction_prompt | llm

st.title("Blog Post Generator")
topic = st.text_input("Input topic")

if topic:
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)
