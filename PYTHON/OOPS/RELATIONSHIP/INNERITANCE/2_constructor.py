# constructor is a method that automatically call when the method is called 
# if we didnt create it by default it will automatically create by itself


"""   1. If we didnt create a constructor in child class and we are passing a pareameter to it then that parameter is initilised to a parent class"""
class Parent:
    def __init__(self, name, place):
        self.name = name
        self.place = place


class Child(Parent):
    pass        

val = Child("lalith", "Besagarahalli")
print(val.name)

