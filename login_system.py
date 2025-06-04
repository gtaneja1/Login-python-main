
import hashlib
from datetime import datetime

def log_login(username):
    with open("logins.log", "a") as log:
        log.write(f"{username} logged in at {datetime.now()}\n")
        if __name__ == "__main__":
            username = "gauri"  # ✅ Define it before using
    log_login(username)
        
         
def register():
    print("\n--- Register ---")
    username = input("Enter a new username: ").strip()
    password = input("Enter a new password: ").strip()

    # Check if the username already exists
    try:
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                stored_username, _ = line.strip().split(",")
                if username == stored_username:
                    print("❌ Username already exists. Try a different one.\n")
                    return
    except FileNotFoundError:
        pass  # File will be created below if it doesn't exist
    
    hashed_password = hash_password(password)
    #it commands to save only encrypted version
    

    # Save new user
    with open("users.txt", "a") as file:
       file.write(f"{username},{hashed_password}\n")  # not raw password

    print(f"✅ Registration successful! You are now logged in as, {username}.\n")
    return username

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#it doesnt save the actual password but instead an encrypted format of it


def login():
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    hashed_input = hash_password(password)

    try:
        with open("users.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and hashed_input == stored_password:

                    print(f"✅ Login successful! Welcome back, {username}.\n")
                    return
            print("❌ Incorrect username or password.\n")
    except FileNotFoundError:
        print("⚠️ No users found. Please register first.\n")
        
        #saving only logged in user info
def save_logged_in_user(username):
    with open("current.user.txt", "w") as file:
        file.write(username)
        
def load_logged_in_user():
    try:
        
        with open("current.user.txt","r") as file:
          return file.read().strip()
    except FileNotFoundError:
        return None
    
def clear_logged_in_user():
    with open("current.user.txt", "w") as file:
        file.write("")
        
def main():
    print("Welcome!")
    logged_in_user = load_logged_in_user()
    
    while True:
        if logged_in_user:
            print(f"🎉 Logged in as {logged_in_user}")
            print("Type 'logout' to log out or 'exit' to quit.")
            choice = input(">>> ").strip().lower()
            if choice == "logout":
                clear_logged_in_user()
                print(f"👋 Logged out {logged_in_user}.\n")
                logged_in_user = None
            elif choice == "exit":
                print("Goodbye!")
                break
            elif choice == "continue":
               print(f"➡️ Continuing session for {logged_in_user}...")
               print("✨ You can now access your dashboard\n")

            else:
                print("⚠️ Invalid choice.")
        else:
            print("\nType 'login', 'register', or 'exit':")
            choice = input(">>> ").strip().lower()
            if choice == "login":
                username = login()
                if username:
                    save_logged_in_user(username)
                    logged_in_user = username
            elif choice == "register":
                username = register()
                if username:
                    save_logged_in_user(username)
                    logged_in_user = username
            elif choice == "exit":
                print("👋 Goodbye!")
                break
            else:
                print("⚠️ Invalid input.")
                
if __name__ == "__main__":
    log_login() 

    
    
   
   


            
     
    
                
 
    
