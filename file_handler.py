def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    return "Your note has been saved."

def chat_history(user_message, assistant_response):
    with open("chat_history.txt", "a") as file:
        file.write(f"User: {user_message}\n")
        file.write(f"Assistant: {assistant_response}\n\n")

def load_chat_history():
    try:
        with open("chat_history.txt", "r") as file:
         history = file.read()

         return history
    except FileNotFoundError:
        return "no chat history found."

def save_username(name):
    with open ("username.txt", "w") as file:
        file.write(name)

    return "User name has been saved." 

def load_username():
    try:
        with open("username.txt", "r") as file:
            name = file.read()

        return name

    except FileNotFoundError:
        return None
      