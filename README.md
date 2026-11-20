Smart Personal Assistant Chatbot

A desktop assistant built in Python that keeps your notes and to-dos, does calculations, and searches inside PDF files, all from one window.

App screenshot

<img width="1906" height="938" alt="image" src="https://github.com/user-attachments/assets/80370c6e-7ac7-45c7-960e-3d5205543ce8" />


Features
Personalized greeting
Scientific calculator
To-do list management
Notes management
Search for text inside PDF files
Date and time information
Random number generation
Simple chatbot replies
Saves your data to files so it is still there next time
Graphical interface built with Tkinter
Tech stack

Python, Tkinter, Object-Oriented Programming, file handling, pypdf, plus the standard datetime, random, math and re modules

Run it locally
bash
git clone https://github.com/fatimahamid25/Smart-Personal-Assistant-Chatbot.git
cd Smart-Personal-Assistant-Chatbot
pip install pypdf
python main.py
Project structure
├── main.py          # starts the app
├── gui.py           # Tkinter interface
├── assistant.py     # chatbot logic
├── user.py          # user profile
├── todo.py          # to-do list
├── file_handler.py  # saving and loading
└── pdf_read.py      # PDF text search
What I learned
Designing a program with classes and separate modules
Building a desktop interface with Tkinter
Saving and loading data with file handling
Extracting and searching text from PDFs
Author

Fatima Hamid, Software Engineering student focused on Python, machine learning and data science. GitHub: @fatimahamid25
