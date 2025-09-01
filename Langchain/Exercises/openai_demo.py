import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

prompt = "Enter the question you want to ask the model: "
question = input(prompt)
response = llm.invoke(question)

print(response)

