# Multiple class is derived from single parent class 
"""              Parent
                /      \
             Child1    Child2
"""

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

