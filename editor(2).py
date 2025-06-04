#using textblob instead of openai which is a very basic module and can catch only minor spelling mistakes

from textblob import TextBlob

def correct_text(text):
    try:
        blob = TextBlob(text)
        corrected_text = str(blob.correct())

        print("\n✅ Corrected text:")
        print(corrected_text)

        # Ask to save
        save = input("\nDo you want to save this corrected text to a file? (y/n): ")
        if save.lower() == "y":
            with open("corrected_output.txt", "w") as file:
                file.write(corrected_text)
            print("✅ Saved as corrected_output.txt")

        return corrected_text

    except Exception as e:
        print("❌ Error while correcting text:", e)
        return text


def open_editor(username):
    print(f"\nWelcome, {username}!")
    print("What would you like to do?")
    print("1. Type new text")
    print("2. Load from file")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        text = input("Type your text here:\n")
        correct_text(text)

    elif choice == '2':
        filename = input("Type your filename (with .txt): ")
        try:
            with open(filename, "r") as file:
                text = file.read()
                print(f"\n📄 Loaded text from {filename}:\n{text}")
                correct_text(text)
        except FileNotFoundError:
            print("❌ File not found.")

    else:
        print("❌ Invalid choice.")
