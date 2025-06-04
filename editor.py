

import openai
openai.api_key = 'your-api-key'

def languagetool():
   
    text = input("Enter your text here:\n")

    #  Send request to OpenAI for grammar correction
    prompt = (
        "Correct the grammar, spelling, and clarity of the following text. "
        "Return only the corrected version without explanations:\n\n"
        f"{text}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        corrected_text = response['choices'][0]['message']['content'].strip()

        
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
