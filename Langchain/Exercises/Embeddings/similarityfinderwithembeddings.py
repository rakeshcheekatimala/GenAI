from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import numpy as np
import ollama

# Note: This program is for experimenting only


# Program 1: Ollama Embeddings

ollamallm = OllamaEmbeddings(model="nomic-embed-text:latest")
text = input("Enter your text to convert into ollama embeddings")
ollama_response = ollama.embeddings(model="nomic-embed-text:latest", prompt=text)
ollama_embedding = ollama_response["embedding"]



# Program 2: OpenAI Embeddings

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openaillm = OpenAIEmbeddings(api_key=OPEN_API_KEY, model="text-embedding-3-small")
openai_embedding = openaillm.embed_query(text)

# Similarity Score for the two embeddings

score = np.dot(ollama_embedding, openai_embedding)

# Lets find the similarity score between the two embeddings

print(f"Similarity % Score is {score*100}")

# ---------- Cosine Similarity ----------
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

score = cosine_similarity(ollama_embedding, openai_embedding)

print(f"\nCosine Similarity between Ollama & OpenAI embeddings: {score:.4f}")
print(f"Percentage Similarity: {score * 100:.2f}%")