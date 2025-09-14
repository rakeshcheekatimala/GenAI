from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import base64
import os
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools


def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode()


llm = ChatOllama(model="llama3:latest")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can identify a landmark."),
        (
            "human",
            [
                {"type": "text", "text": "return the landmark name"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,""{image}",
                        "detail": "low",
                    },
                },
            ],
        ),
    ]
)

chain = prompt | llm

st.title("Landmark Helper")
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"])

question = st.text_input("Enter a question about the landmark")

# Agent Creation Code


# Pull these below prompt from the hub.
prompt = hub.pull("hwchase17/react")
tools = load_tools(["wikipedia", "ddg-search"])
agent = create_react_agent(llm, tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

task = None
if question:
    image = encode_image(uploaded_file)
    response = chain.invoke({"image": image})
    print('response is ', response)
    task = question + response.content

if task:
    response = agent_executor.invoke({"input": task + "with out explanation"})
    st.write(response["output"])
