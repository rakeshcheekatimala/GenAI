# What is Langchain?
LangChain is a framework for developing applications powered by large language models (LLMs).


The LangChain framework consists of multiple open-source libraries. Read more in the Architecture page.

- langchain-core: Base abstractions for chat models and other components.
- Integration packages (e.g. langchain-openai, langchain-anthropic, etc.): Important integrations have been split into lightweight packages that are co-maintained by the LangChain team and the integration developers.

```
from langchain_openai import ChatOpenAI

```

This is used for for creating an instance of ChatModel where you can define model name which you are interested to create.

Example

```py 
# Load Env
load_dotenv()

# Read the API KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

```

- langchain: Chains, agents, and retrieval strategies that make up an application's cognitive architecture.
- langchain-community: Third-party integrations that are community maintained.

```
from langchain_community.agent_toolkits.load_tools import load_tools
tools = load_tools(["wikipedia", "ddg-search"])
```

Here above wikipedia, ddg-search are tools which will be used by LLM once the reasoning & action needs to be executed for a given task using these tools.

# What is tools

- Refer to Agents folder readme.md

- langgraph: Orchestration framework for combining LangChain components into production-ready applications with persistence, streaming, and other key features. See LangGraph documentation.


# Langchain Demos

This repository contains various demos showcasing Langchain integration.

# Agents 

Under this folder Langchain, goto Agents to understand what is Agent, how to build & run it.


# Streamlit 

Under this folder Langchain, goto Streamlit to understand what is streamlit, why we need, how to run the app built using streamlit.

### Prerequisites

- Python 3.x
- Streamlit
- Langchain
- Ollama Installation [Installation](https://ollama.com/download)
- OPEN_API_KEY (Ensure you have topped up some credits to run the application)


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
