# Gemini AI Icebreaker Bot

A Retrieval-Augmented Generation (RAG) command-line application that acts as an intelligent AI networking copilot. It uses Google's Gemini LLMs and Gemini Embeddings via LlamaIndex to instantly read a person's LinkedIn profile (mock JSON data) and generate tailored icebreakers, professional facts, and answer deeper questions about their career history.

**Key Features:**
- 🧠 Powered by Google Gemini (`models/gemini-2.5-flash`)
- 🔍 Text vectorization using Gemini Embeddings (`models/gemini-embedding-001`)
- 📚 RAG Pipeline built with LlamaIndex
- 💬 Interactive CLI for dynamic Q&A about the parsed profile

## Prerequisites

- Python 3.8+
- A Google Gemini API Key

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShangeetVishnuSankar/ai-networking-copilot.git
   cd ai-networking-copilot
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install llama-index llama-index-llms-gemini llama-index-embeddings-gemini requests python-dotenv
   ```

4. **Configure your API Key:**
   Create a `.env` file in the root directory of the project and add your Gemini API key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Usage

Simply run the main Python script to start the bot:

```bash
python main.py
```

1. The bot will automatically fetch the mock LinkedIn profile data.
2. It will vectorize and index the career history using Gemini Embeddings.
3. It will generate 3 highly relevant initial facts/icebreakers securely using Gemini 2.5 Flash.
4. You will enter an interactive chat where you can ask custom, deeper questions about the person's profile. Type `exit` or `quit` to leave the chat.

## Project Structure

- `main.py`: The entry point and conductor of the app, containing the interactive CLI.
- `config.py`: Central configuration file managing API keys, model variables, and prompt templates.
- `llm_interface.py`: Initializes and configures global LlamaIndex settings for Gemini LLMs and Embeddings.
- `data_extraction.py`: Handles fetching the external LinkedIn profile data.
- `data_processing.py`: Splits the data into chunks and builds the `VectorStoreIndex`.
- `query_engine.py`: Functions to generate the initial facts and answer user ad-hoc queries based on the vector store.
