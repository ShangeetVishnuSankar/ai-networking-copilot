import sys
from llm_interface import set_global_gemini_settings
from data_extraction import extract_linkedin_profile
from data_processing import create_index_from_profile
from query_engine import generate_initial_facts, answer_user_query

def main():
    print("===========================================")
    print(" Welcome to the Gemini AI Icebreaker Bot")
    print("===========================================")
    
    # 1. Initialize Gemini settings (LLM + Embedding)
    set_global_gemini_settings()

    # 2. Extract Data
    profile_data = extract_linkedin_profile()
    if not profile_data:
        print("Exiting due to missing data.")
        sys.exit(1)

    # 3. Process Data into VectorStoreIndex
    index = create_index_from_profile(profile_data)

    # 4. Generate Initial Facts
    print("\n--- Let's break the ice! ---")
    facts = generate_initial_facts(index)
    print(facts)
    print("------------------------------\n")

    # 5. Interactive Chat Bot Feature
    print("You can now ask deeper questions about this profile (Type 'exit' or 'quit' to quit)")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower().strip() in ['exit', 'quit']:
                print("Bot: Goodbye! Have a great time networking!")
                break
                
            answer = answer_user_query(index, user_input)
            print(f"Bot: {answer}\n")
        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    main()