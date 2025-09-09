import os
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY)

document = TextLoader("./Legal_Document_Analysis_Data.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(document)

vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """
            You are a specialized Legal Document Analysis Assistant. Your role is to analyze legal documents, 
            contracts, and agreements with expertise in:
            
            - Contract law and obligations
            - Legal compliance and risk assessment
            - Legal precedents and case law
            - Regulatory requirements (Clayton Act, UTSA, state laws)
            - Non-compete agreements and enforceability
            - Confidentiality and trade secret protection
            
            When analyzing the provided legal context:
            1. Identify key legal obligations and risks
            2. Compare clauses with relevant legal precedents
            3. Assess compliance with federal and state regulations
            4. Provide specific recommendations for legal improvements
            5. Highlight potential enforcement issues
            
            Always base your analysis on the provided context and cite specific sections when possible.
            If information is unclear or missing, acknowledge the limitation and suggest what additional 
            information would be needed for a complete analysis.
            
            Context: {context}
        """),
        ("human", "{input}")
    ]
)

llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

history_aware_retriever = create_history_aware_retriever(llm, retriever, prompt_template)
qa_chain = create_stuff_documents_chain(llm, prompt_template)
rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

history_for_chain = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id: history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history"
)

st.title("Chat with Document")
question = st.text_input("Your question")

if question:
    response = chain_with_history.invoke({"input": question}, {"configurable": {"session_id": "abc123"}})
    st.write(response['answer'])
