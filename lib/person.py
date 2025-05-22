#!/usr/bin/env python3
class Person:
    def __init__(self, name="Unnamed"):  # Default name to prevent errors
        self.name = name

    def talk(self):  # Instance method
        print("Hello World!")

    def walk(self):  # Instance method
        print("The person is walking.")

# Example usage
guido = Person("Guido")
guido.talk()  # Output: Hello World!
guido.walk()  # Output: The person is walking.

