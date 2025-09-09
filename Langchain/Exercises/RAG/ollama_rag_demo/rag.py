import os
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_ollama import OllamaEmbeddings
from pathlib import Path

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

pdf_path = Path(__file__).parent / "academic_research_data.pdf"

document = PyPDFLoader(str(pdf_path)).load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(document)

vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are an assistant for answering questions. Use the provided context to respond.
            If the answer isn't clear , acknowledge that you don't know. Limit your response to
            three concise sentences. {context}    
        """),
        ("human", "{input}")
    ]
)

llm = ChatOllama(model="llama3:latest")

history_aware_retriever = create_history_aware_retriever(llm, retriever, prompt_template)
qa_chain = create_stuff_documents_chain(llm, prompt_template)
rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)


print("Chat with Document")
question = input("Your question")

if question:
    response = rag_chain.invoke({"input": question})
    print(response['answer'])

