from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="mistral:latest")

prompt = "Enter the question you want to ask the model: "
question = input(prompt)
response = llm.invoke(question)

print(response)

