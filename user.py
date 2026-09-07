import string
class User:
    def __init__(self,name):
        self.name = name.title()

    def introduce(self):
        return f"My Name is {self.name}."