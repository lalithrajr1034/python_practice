#Acess Modifiers:


"""Types of Acess Modifirers"""
#1.Public acess modifiers                       Any where
#2.Protected acess modifiers  (_class_abcd)     class and subclass 
#3.Private acess modifiers    (_class__abcd)    class    

class lalith:
    def __init__(self,age,name):
        self.__age=age
        self.__name=name
    def introduction(self):
        print(f"My name is {self.__name} and i am {self.__age} years old")   
obj=lalith(19,"lalith raj")
obj.__age=20                   
obj.introduction()        


class Demo:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

obj = Demo()

print(obj.public_var)      
print(obj._protected_var)  # or   obj._Demo_protected_var
print(obj._Demo__private_var) 
