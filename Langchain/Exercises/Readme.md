# Langchain Demos

This repository contains various demos showcasing Langchain integration with different LLM models.

## Streamlit Chat Application

A simple chat application built with Streamlit that allows you to interact with the Mistral language model.

### Prerequisites

- Python 3.x
- Streamlit
- Langchain
- Ollama (with Mistral model installed)

### Installation

1. Install the required packages:
```bash
pip install streamlit langchain-community
```

2. Make sure you have Ollama installed and the Mistral model pulled:
```bash
# Install Ollama from https://ollama.ai/
# Then pull the Mistral model
ollama pull mistral
```

### Running the Application

To run the Streamlit application:

```bash
streamlit run streamlit.py
```

The application will open in your default web browser. You can then:
1. Enter your question in the text input field
2. The response from the Mistral model will be displayed below

### Features

- Simple and intuitive chat interface
- Powered by Mistral language model through Ollama
- Real-time responses