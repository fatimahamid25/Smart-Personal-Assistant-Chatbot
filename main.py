from assistant import SmartAssistant
from user import User
from file_handler import save_note, chat_history, load_chat_history, save_username, load_username
from gui import ZyraGUI

app = ZyraGUI()
app.run()

name = input("Enter your name: ")

user = User(name)

print(save_username(name))

assistant = SmartAssistant(name)

print(user.introduce())

assistant.greet()

while True:
    message = input("You: ")

    if message.lower().startswith("note "):
        note = message[5:]
        print("Assistant:", save_note(note))
        continue

    if message.lower() == "history":
        print("Assistant:")
        print(load_chat_history())
        continue

    if "what is my name" in message.lower():
        name = load_username()

        if name:
            response = f"Your name is {name}."
        else:
            response = "I don't know your name yet."

        print("Assistant:", response)
        chat_history(message, response)
        continue

    response = assistant.respond(message)

    print("Assistant:", response)

    chat_history(message, response)

    if "bye" in message.lower():
        break