import tkinter as tk
from tkinter import messagebox

from assistant import SmartAssistant
from user import User
from todo import add_task, get_tasks, delete_task
from file_handler import save_note, chat_history, load_chat_history, save_username, load_username


class ZyraGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Zyra - Smart Personal Assistant")
        self.root.geometry("1000x650")
        self.root.configure(bg="#1E1E2F")

        # Load username
        name = load_username()

        if not name:
            name = "User"

        self.user = User(name)
        self.assistant = SmartAssistant(name)

        self.create_gui()

    def create_gui(self):

        # ================= HEADER =================

        header = tk.Frame(
            self.root,
            bg="#29293D",
            height=70
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="✦ ZYRA",
            font=("Arial", 24, "bold"),
            bg="#29293D",
            fg="#A855F7"
        )

        title.pack(side="left", padx=25, pady=15)

        subtitle = tk.Label(
            header,
            text="Smart Personal Assistant",
            font=("Arial", 12),
            bg="#29293D",
            fg="white"
        )

        subtitle.pack(side="left")


        # ================= MAIN FRAME =================

        main_frame = tk.Frame(
            self.root,
            bg="#1E1E2F"
        )

        main_frame.pack(fill="both", expand=True)


        # ================= SIDEBAR =================

        sidebar = tk.Frame(
            main_frame,
            bg="#29293D",
            width=220
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)


        menu_label = tk.Label(
            sidebar,
            text="FEATURES",
            font=("Arial", 12, "bold"),
            bg="#29293D",
            fg="#A855F7"
        )

        menu_label.pack(pady=20)


        tk.Button(
            sidebar,
            text="💬 New Chat",
            command=self.new_chat,
            bg="#3B3B55",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            width=20,
            pady=10
        ).pack(pady=5)


        tk.Button(
            sidebar,
            text="🧮 Calculator",
            command=self.open_calculator,
            bg="#3B3B55",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            width=20,
            pady=10
        ).pack(pady=5)


        tk.Button(
            sidebar,
            text="✓ To-Do List",
            command=self.open_todo,
            bg="#3B3B55",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            width=20,
            pady=10
        ).pack(pady=5)


        tk.Button(
            sidebar,
            text="📝 Save Note",
            command=self.open_note,
            bg="#3B3B55",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            width=20,
            pady=10
        ).pack(pady=5)


        tk.Button(
            sidebar,
            text="📜 History",
            command=self.open_history,
            bg="#3B3B55",
            fg="white",
            font=("Arial", 11),
            relief="flat",
            width=20,
            pady=10
        ).pack(pady=5)


        # ================= CHAT AREA =================

        chat_frame = tk.Frame(
            main_frame,
            bg="#1E1E2F"
        )

        chat_frame.pack(
            side="left",
            fill="both",
            expand=True
        )


        self.chat_box = tk.Text(
            chat_frame,
            bg="#1E1E2F",
            fg="white",
            font=("Arial", 12),
            wrap="word",
            relief="flat",
            padx=20,
            pady=20
        )

        self.chat_box.pack(
            fill="both",
            expand=True
        )


        # Welcome Message

        self.chat_box.insert(
            "end",
            "✦ ZYRA\n"
        )

        self.chat_box.insert(
            "end",
            f"Hello {self.user.name}! I am Zyra, your Smart Personal Assistant.\nHow can I help you?\n\n"
        )


        # ================= INPUT AREA =================

        input_frame = tk.Frame(
            chat_frame,
            bg="#29293D",
            height=70
        )

        input_frame.pack(
            fill="x"
        )


        self.entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="white",
            fg="black"
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=15,
            pady=15,
            ipady=8
        )

        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )


        send_button = tk.Button(
            input_frame,
            text="Send ➤",
            command=self.send_message,
            bg="#A855F7",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8
        )

        send_button.pack(
            side="right",
            padx=15
        )


    # ================= SEND MESSAGE =================

    def send_message(self):

        message = self.entry.get()

        if message == "":
            return


        self.chat_box.insert(
            "end",
            f"You: {message}\n"
        )


        self.entry.delete(
            0,
            "end"
        )


        response = self.assistant.respond(message)


        self.chat_box.insert(
            "end",
            f"Zyra: {response}\n\n"
        )


        self.chat_box.see("end")


        chat_history(
            message,
            response
        )


    # ================= NEW CHAT =================

    def new_chat(self):

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.insert(
            "end",
            "✦ ZYRA\n"
        )

        self.chat_box.insert(
            "end",
            "New chat started!\nHow can I help you?\n\n"
        )


    # ================= TODO =================

    def open_todo(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Zyra To-Do List"
        )

        window.geometry(
            "500x500"
        )

        window.configure(
            bg="#29293D"
        )


        title = tk.Label(
            window,
            text="✓ MY TO-DO LIST",
            font=("Arial", 18, "bold"),
            bg="#29293D",
            fg="#A855F7"
        )

        title.pack(
            pady=20
        )


        task_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )

        task_entry.pack(
            fill="x",
            padx=20,
            pady=10,
            ipady=7
        )


        listbox = tk.Listbox(
            window,
            font=("Arial", 12),
            bg="#1E1E2F",
            fg="white"
        )

        listbox.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


        def refresh_tasks():

            listbox.delete(
                0,
                "end"
            )


            tasks = get_tasks()


            for i, task in enumerate(tasks):

                listbox.insert(
                    "end",
                    f"{i + 1}. {task}"
                )


        def add():

            task = task_entry.get()

            result = add_task(task)

            task_entry.delete(
                0,
                "end"
            )

            refresh_tasks()

            messagebox.showinfo(
                "Zyra",
                result
            )


        def delete():

            selected = listbox.curselection()

            if not selected:

                messagebox.showwarning(
                    "Zyra",
                    "Please select a task."
                )

                return


            index = selected[0]

            result = delete_task(index)

            refresh_tasks()

            messagebox.showinfo(
                "Zyra",
                result
            )


        tk.Button(
            window,
            text="Add Task",
            command=add,
            bg="#A855F7",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            pady=5
        )


        tk.Button(
            window,
            text="Delete Task",
            command=delete,
            bg="#DC2626",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            pady=5
        )


        refresh_tasks()


    # ================= NOTE =================

    def open_note(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Save Note"
        )

        window.geometry(
            "500x350"
        )


        tk.Label(
            window,
            text="Write Your Note",
            font=("Arial", 16, "bold")
        ).pack(
            pady=15
        )


        note_box = tk.Text(
            window,
            font=("Arial", 12)
        )

        note_box.pack(
            fill="both",
            expand=True,
            padx=20
        )


        def save():

            note = note_box.get(
                "1.0",
                "end"
            ).strip()


            if note:

                result = save_note(note)

                messagebox.showinfo(
                    "Zyra",
                    result
                )

                window.destroy()


        tk.Button(
            window,
            text="Save Note",
            command=save,
            bg="#A855F7",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            pady=15
        )


    # ================= HISTORY =================

    def open_history(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Chat History"
        )

        window.geometry(
            "600x500"
        )


        history = load_chat_history()


        text = tk.Text(
            window,
            font=("Arial", 11),
            wrap="word"
        )

        text.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )


        text.insert(
            "1.0",
            history
        )


    # ================= CALCULATOR =================

    def open_calculator(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Scientific Calculator"
        )

        window.geometry(
            "450x400"
        )

        window.configure(
            bg="#29293D"
        )


        tk.Label(
            window,
            text="🧮 SCIENTIFIC CALCULATOR",
            font=("Arial", 16, "bold"),
            bg="#29293D",
            fg="#A855F7"
        ).pack(
            pady=20
        )


        tk.Label(
            window,
            text="First Number",
            bg="#29293D",
            fg="white"
        ).pack()


        num1 = tk.Entry(
            window,
            font=("Arial", 12)
        )

        num1.pack(
            padx=30,
            fill="x",
            ipady=7
        )


        tk.Label(
            window,
            text="Second Number",
            bg="#29293D",
            fg="white"
        ).pack(
            pady=10
        )


        num2 = tk.Entry(
            window,
            font=("Arial", 12)
        )

        num2.pack(
            padx=30,
            fill="x",
            ipady=7
        )


        operations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division"
        ]


        operation = tk.StringVar()

        operation.set(
            "Addition"
        )


        tk.OptionMenu(
            window,
            operation,
            *operations
        ).pack(
            pady=15
        )


        result_label = tk.Label(
            window,
            text="Result: ",
            font=("Arial", 13, "bold"),
            bg="#29293D",
            fg="white"
        )

        result_label.pack(
            pady=10
        )


        def calculate():

            try:

                number1 = float(
                    num1.get()
                )

                number2 = float(
                    num2.get()
                )


                if operation.get() == "Addition":

                    result = number1 + number2


                elif operation.get() == "Subtraction":

                    result = number1 - number2


                elif operation.get() == "Multiplication":

                    result = number1 * number2


                elif operation.get() == "Division":

                    result = number1 / number2


                result_label.config(
                    text=f"Result: {result}"
                )


            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Please enter valid numbers."
                )


            except ZeroDivisionError:

                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero."
                )


        tk.Button(
            window,
            text="Calculate",
            command=calculate,
            bg="#A855F7",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            pady=10
        )


    def run(self):

        self.root.mainloop()