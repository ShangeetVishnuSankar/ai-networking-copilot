import config
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

def set_global_gemini_settings():
    """Configures LlamaIndex to use Gemini models securely."""
    print("Setting up Gemini LLM and Embeddings...")
    
    # Set standard Gemini configuration
    Settings.llm = Gemini(
        model=config.LLM_MODEL, 
        api_key=config.GOOGLE_API_KEY, 
        temperature=0.1 # Low temperature for factual RAG responses
    )
    
    # Configure Gemini Embeddings
    Settings.embed_model = GeminiEmbedding(
        model_name=config.EMBEDDING_MODEL, 
        api_key=config.GOOGLE_API_KEY
    )