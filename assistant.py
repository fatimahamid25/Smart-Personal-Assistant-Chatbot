from datetime import datetime
import random
import math

from pdf_read import search_pdf


class SmartAssistant:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! {self.name}, I am Zyra, your Smart Personal Assistant.")

    def scientific_calculator(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            while True:
                print("\n===== SCIENTIFIC CALCULATOR =====")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Power")
                print("6. Sin")
                print("7. Cos")
                print("8. Tan")
                print("9. Ceiling")
                print("10. Floor")
                print("11. Exit")

                choice = input("\nChoose an operation: ")

                try:
                    if choice == "1":
                        print("Result:", num1 + num2)

                    elif choice == "2":
                        print("Result:", num1 - num2)

                    elif choice == "3":
                        print("Result:", num1 * num2)

                    elif choice == "4":
                        if num2 == 0:
                            raise ZeroDivisionError("Cannot divide by zero.")

                        print("Result:", num1 / num2)

                    elif choice == "5":
                        power = float(input("Enter power: "))
                        print("Result:", math.pow(num1, power))

                    elif choice == "6":
                        print(
                            "sin(",
                            num1,
                            ") =",
                            math.sin(math.radians(num1))
                        )

                    elif choice == "7":
                        print(
                            "cos(",
                            num1,
                            ") =",
                            math.cos(math.radians(num1))
                        )

                    elif choice == "8":
                        print(
                            "tan(",
                            num1,
                            ") =",
                            math.tan(math.radians(num1))
                        )

                    elif choice == "9":
                        print(
                            "Ceiling of",
                            num1,
                            "=",
                            math.ceil(num1)
                        )

                    elif choice == "10":
                        print(
                            "Floor of",
                            num1,
                            "=",
                            math.floor(num1)
                        )

                    elif choice == "11":
                        print("Exiting Scientific Calculator...")
                        break

                    else:
                        print("Invalid choice!")

                except ValueError:
                    print("Please enter a valid number.")

                except ZeroDivisionError as e:
                    print("Error:", e)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    def square_root(self):
        try:
            number = float(input("Enter a number: "))

            if number < 0:
                return "Cannot find the square root of a negative number."

            return f"The square root is {math.sqrt(number)}"

        except ValueError:
            return "Please enter a valid number."

    def cube_root(self):
        try:
            number = float(input("Enter a number: "))

            return f"The cube root is {number ** (1 / 3)}"

        except ValueError:
            return "Please enter a valid number."

    def factorial(self):
        try:
            number = int(input("Enter a number: "))

            if number < 0:
                return "Factorial cannot be calculated for a negative number."

            return f"The Factorial of the number is: {math.factorial(number)}"

        except ValueError:
            return "Please enter a valid whole number."

    def pdf_info(self, question):
        answer = search_pdf(question)

        if answer:
            return answer

        return "Sorry, I could not find information about that in the PDF."

    def respond(self, message):
        message = message.lower().strip()

        responses = {
            "hello": "Hello! How can I help you?",
            "hi": "Hello! How can I help you?",
            "hey": "Hello! How can I help you?",
            "hy": "Hello! How can I help you?",

            "your name": "I am Zyra, your Smart Personal Assistant.",
            "what is your name": "I am Zyra, your Smart Personal Assistant.",
            "who are you": "I am Zyra, your Smart Personal Assistant.",

            "what is my name": f"Your name is {self.name}.",
            "who am i": f"You are {self.name}.",

            "how are you": "I am fine, Thanks for asking.",
            "how are you?": "I am fine, Thanks for asking.",

            "bye": "Goodbye! Have a nice day.",

            "help": """--- Smart Personal Assistant Features ---

1. Greeting
2. Tell current time
3. Tell today's date
4. Generate a random number
5. Tell a random joke
6. Scientific calculator
7. Find square root
8. Find cube root
9. Find factorial
10. Tell assistant's name
11. Get information from Machine Learning PDF
12. To-do List
13. Exit"""
        }

        if message in responses:
            return responses[message]

        if "time" in message:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        elif "date" in message:
            current_date = datetime.now().strftime("%d-%m-%Y")
            return f"Today's date is {current_date}."

        elif "random number" in message:
            number = random.randint(1, 100)
            return f"Your number is {number}."

        elif "joke" in message:
            jokes = [
                "I am smart, not smart enough to fix your code.",
                "You call it a bug, I call it a surprise feature.",
                "My code runs once and suddenly I am a software engineer.",
                "I said I am a Smart Assistant, not a miracle worker."
            ]

            return random.choice(jokes)

        elif "calculator" in message or "calculate" in message:
            self.scientific_calculator()
            return "Calculator closed."

        elif "square root" in message:
            return self.square_root()

        elif "cube root" in message:
            return self.cube_root()

        elif "fact" in message or "factorial" in message:
            return self.factorial()

        elif "machine learning" in message or "pdf" in message:
            return self.pdf_info(message)

        elif "todo" in message or "to-do" in message:
            return "Please open the To-Do List from the sidebar."

        else:
            pdf_answer = self.pdf_info(message)

            if pdf_answer != "Sorry, I could not find information about that in the PDF.":
                return pdf_answer

            return "Sorry, I don't understand your message."