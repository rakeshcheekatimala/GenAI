# Langchain Demos

This repository contains various demos showcasing Langchain integration with different LLM models.

### Prerequisites

- Python 3.x
- Streamlit
- Langchain
- Ollama Installation [Installation](https://ollama.com/download)

### Installation of Required packages 

1. Install the required packages:

```bash
pip install streamlit langchain-community
```

2. How to verify if you have any ollama models installed 

```
ollama list

```
I have below models installed 
```

NAME                       ID              SIZE      MODIFIED
nomic-embed-text:latest    0a109f422b47    274 MB    4 days ago
llama2:latest              78e26419b446    3.8 GB    10 days ago
gemma:2b                   b50d6c999e59    1.7 GB    3 months ago
llama3.2:1b                baf6a787fdff    1.3 GB    4 months ago
llama3:latest              365c0bd3c000    4.7 GB    4 months ago
mistral:latest             f974a74358d6    4.1 GB    9 months ago

```

# How to Install any opensource model

```bash
# Install Ollama from https://ollama.ai/
# Then pull the Mistral model
ollama pull mistral
```

### Running the Application built using streamlit

To run the Streamlit application:

```bash
streamlit run programname.py
```
