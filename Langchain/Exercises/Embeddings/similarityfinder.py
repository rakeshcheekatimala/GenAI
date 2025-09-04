import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import numpy as np
load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
llm = OpenAIEmbeddings(api_key = OPEN_API_KEY)
text = input("Enter your text to convert into embeddings")
embedding1 = llm.embed_query(text)
text2 = input("Enter your text to convert into embeddings")
embedding2 = llm.embed_query(text2)
score = np.dot(embedding1, embedding2)

print(f"Similarity % Score is {score*100}")

