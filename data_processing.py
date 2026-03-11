import json
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
import config

def create_index_from_profile(profile_data):
    """Splits the profile JSON into chunks and creates a VectorStoreIndex."""
    # 1. Convert simple dictionary JSON into a formatted plain text string
    profile_text = json.dumps(profile_data, indent=2)
    
    # 2. Package string into a LlamaIndex Document object
    document = Document(text=profile_text)
    
    # 3. Use SentenceSplitter to chop our text into chunks
    splitter = SentenceSplitter(chunk_size=config.CHUNK_SIZE)
    nodes = splitter.get_nodes_from_documents([document])
    
    print(f"Created {len(nodes)} document chunks. Creating Vector Store using Gemini Embeddings...")
    
    # 4. Generate the index 
    # Because we ran set_global_gemini_settings() earlier, this automatically uses Gemini
    index = VectorStoreIndex(nodes=nodes)
    return index