# Multi lavel inneritance are the class that are derived form another derived class

class Grandparent:
    def name(self):
        print("shella ki javani")
class Parent(Grandparent):
    def __init__(self, nam, info):
        self.nam = nam
        self.info = info
    def name(self):
         print("my name is sheela")   
         super().name()       
class Child(Parent):
    def __init__(self, nam, info, fvtsong):
        super().__init__(nam, info)        
        
    def name(self):
        print("hello 1 2 3 miku testing")
        super().name()
obj = Child("Lalith", "i am a birthaday boy", "yaro nenu")        
obj.name()