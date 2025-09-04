import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
llm = OpenAIEmbeddings(api_key = OPEN_API_KEY)
text = input("Enter your text to convert into embeddings")
response = llm.embed_query(text)
print(response)

