from llama_index.core import PromptTemplate
import config

def generate_initial_facts(index):
    """Generates 3 interesting facts using the Vector DB."""
    facts_prompt = PromptTemplate(template=config.INITIAL_FACTS_TEMPLATE)
    
    # Set up our query process
    query_engine = index.as_query_engine(
        similarity_top_k=config.SIMILARITY_TOP_K,
        text_qa_template=facts_prompt
    )
    
    # Execute the query against Gemini
    query = "Provide three interesting facts about this person's career or education."
    response = query_engine.query(query)
    return response.response

def answer_user_query(index, user_query):
    """Answers a specific question from the user based on the vector index."""
    question_prompt = PromptTemplate(template=config.USER_QUESTION_TEMPLATE)
    
    query_engine = index.as_query_engine(
        similarity_top_k=config.SIMILARITY_TOP_K,
        text_qa_template=question_prompt
    )
    
    response = query_engine.query(user_query)
    return response.response