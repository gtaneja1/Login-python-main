import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_synonym(word):
    prompt= ( "Give me a list of synonyms for the word '{word}'. "
        "Return only the synonyms separated by commas."   
        ) 
