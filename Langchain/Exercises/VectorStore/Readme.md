# Run this Job Search Helper

```
(langchain) rakeshcheekatimala@RAKESHs-MacBook-Pro VectorStore % py job_search_helper.py
Enter the text to search for similar job listings: python and machine learning 
```

Output: Top 3 similar job listings: 

```

[Document(metadata={'source': './job_listings.txt'}, page_content='in Java, Python, and SQL.'),
 Document(metadata={'source': './job_listings.txt'}, page_content='2. Data Scientist at DataMinds - Duties involve analyzing large datasets, building predictive models, and presenting insights to stakeholders. 
 Requires expertise in Python, R, and machine learning.'),
 Document(metadata={'source': './job_listings.txt'}, page_content='in network security and experience with security tools.')]

```

# How To Run Retriever and Use this with chroma DB

```
(langchain) rakeshcheekatimala@RAKESHs-MacBook-Pro VectorStore % py job_search_helper_retriever.py 
Enter the text to search for similar job listings: Cyber Security 
```

```
8. Cybersecurity Specialist at SecureNet - Role involves protecting the company's IT infrastructure, monitoring for security breaches, and implementing security protocols. Requires expertise in
of project management software.
SEM, and content creation.

```

# How to run Job Search helper built using ollama

```
(langchain) rakeshcheekatimala@RAKESHs-MacBook-Pro VectorStore % py job_search_helper_retriever_ollama.py 
Enter the text to search for similar job listings: Cyber Security 
financial modeling.
in network security and experience with security tools.
of project management software.
in Java, Python, and SQL.

```