import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Store API key globally
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Define Gemini Models
LLM_MODEL = "models/gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Number of chunks to retrieve for RAG
CHUNK_SIZE = 400
SIMILARITY_TOP_K = 3

# Using the public mock data URL from the instructions
MOCK_DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZRe59Y_NJyn3hZgnF1iFYA/linkedin-profile-data.json"

# Prompt template to generate initial facts
INITIAL_FACTS_TEMPLATE = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Based on this context, provide exactly three interesting facts about this person's career or education. "
    "Do not hallucinate any information."
)

# Prompt template for answering user questions
USER_QUESTION_TEMPLATE = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given this context, answer the following question: {query_str}\n"
    "If the answer is not contained within the context, simply say 'I don't know based on the provided profile.'."
)