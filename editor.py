

from random import choice
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()


# using chat completion API

def languagetool(text):

    #  Send request to OpenAI for grammar correction
    prompt = (
        "Correct grammar and spelling"
         "Also suggest better synonyms where appropriate. "
        "Rewrite the following text in formal English, correcting grammar and spelling. "
         "Return only the corrected version:\n\n"
    )
   
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        corrected_text = response.choices[0].message.content.strip()

        
        print("\n✅ Corrected text:")
        print(corrected_text)

        # Step 4: Ask to save
        save = input("\nDo you want to save this corrected text to a file? (y/n): ")
        if save.lower() == "y":
            with open("corrected_output.txt", "w") as file:
                file.write(corrected_text)
            print("✅ Saved as corrected_output.txt")

        return corrected_text

    except Exception as e:
        print("❌ Error while contacting OpenAI:", e)
        return text

def open_editor(username):
    print(f"\nWelcome, {username}!")
    print("What would you like to do?")
    print("1. Type new text")
    print("2. Load from file")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        text = input("Type your text here:\n")
        languagetool(text)

    elif choice == '2':
        filename = input("Type your filename (with .txt): ")
        try:
            with open(filename, "r") as file:
                text = file.read()
                print(f"\n📄 Loaded text from {filename}:\n{text}")
                languagetool(text)
        except FileNotFoundError:
            print("❌ File not found.")

    else:
        print("❌ Invalid choice.")
        return   tell me how to edit this 
