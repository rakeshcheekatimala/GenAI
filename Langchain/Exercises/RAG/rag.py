import os
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain, create_history_aware_retriever
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY)

document = TextLoader("product-data.txt").load()
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

llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

create_history_aware_retriever = create_history_aware_retriever(llm, retriever, prompt_template)
qa_chain = create_stuff_documents_chain(llm, prompt_template)
rag_chain = create_retrieval_chain(create_history_aware_retriever, qa_chain)


print("Chat with Document")
question = input("Your question")

if question:
    response = rag_chain.invoke({"input": question})
    print(response['answer'])

