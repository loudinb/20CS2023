class SimpleClass:
    def __new__(cls, *args, **kwargs):
        print("Creating an instance...")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing the object...")
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def __del__(self):
        print(f"Object with name {self.name} is being destroyed...")