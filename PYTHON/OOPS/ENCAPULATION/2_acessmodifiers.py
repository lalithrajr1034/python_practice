#Acess Modifiers:


"""Types of Acess Modifirers"""
#1.Public acess modifiers
#2.Protected acess modifiers  (_)
#3.Private acess modifiers    (__)

class lalith:
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
    def introduction(self):
        print(f"My name is {self.__name} and i am {self.__age} years old")   
obj=lalith(19,"lalith raj")
obj.__age=20                   
obj.introduction()        