import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Listing models:")
try:
    for m in genai.list_models():
        # print(m.name, m.supported_generation_methods)
        if "embedContent" in m.supported_generation_methods:
            print("Embedding model:", m.name)
        if "generateContent" in m.supported_generation_methods:
            print("Generation model:", m.name)
except Exception as e:
    print("Error:", e)
