from langchain_ollama import OllamaEmbeddings
llm = OllamaEmbeddings(model="llama2")

text = input("Enter your text to convert into embeddings")
response = llm.embed_query(text)
print(response)

