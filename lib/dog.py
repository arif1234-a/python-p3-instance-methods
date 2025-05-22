#!/usr/bin/env python3

class Dog:
    def __init__(self, name="Unnamed"):  # Default name to prevent errors
        self.name = name

    def bark(self):  # Instance method
        print("Woof!")

    def sit(self):  # Instance method
        print("The dog is sitting.")

# Example usage
fido = Dog("Buddy")
fido.bark()  # Output: Woof!
fido.sit()  # Output: The dog is sitting.