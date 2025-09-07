from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

llm = OllamaEmbeddings(model="llama3:latest")  
document = TextLoader("job_listings.txt").load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunks = text_splitter.split_documents(document)

vectorstore = Chroma.from_documents(chunks, llm)
retriever = vectorstore.as_retriever()
text = input("Enter the query") 
docs = retriever.invoke(text)

for doc in docs:
    print(doc.page_content)


# print(f"Document has {len(chunks)} chunks")
# print(chunks)

# print(f"Document has {len(document[0].page_content)} characters")
# print(f"Document has {len(document)} pages")

