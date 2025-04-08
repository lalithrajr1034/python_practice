#........................OBJECT............................
#object is a instance of class
#instance==A class is like a recipe""An object is the cake made using that recipe""That cake is an instance of the recipe (class)."""
#In every time while creating a object it will occupy different location

class Computer:
    def memory():
        print("Hi")

c1=Computer
print(c1.memory())


class School:
    def __init__(self):
        print("Hi lalih")
    def artificial_inteligence(self):
        self.a=3
        print("This is class")

School.artificial_inteligence()#THis is an object