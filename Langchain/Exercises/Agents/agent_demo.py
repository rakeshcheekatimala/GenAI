import os
from langchain_openai import ChatOpenAI
from langchain import hub
import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv

# Load Env
load_dotenv()

# Read the API KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

# Pull these below prompt from the hub.
prompt = hub.pull("hwchase17/react")

tools = load_tools(["wikipedia", "ddg-search"])

agent = create_react_agent(llm, tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

st.title("AI Agent with Tools")
task = st.text_input("Enter your task:")

if task:
    with st.spinner("Processing..."):
        response = agent_executor.invoke({"input": task})
    st.write("Response:")
    st.write(response["output"])
