# this super function is used to acess a method of parent class
""" This function must use inside a method """
# this is helpfull because of to avoid method overwriding
# we can also initilise a element


class Parent:
    def __init__(self):
        self.age = 19
    def name_func(self):
        print("my name is raju") 
           
class Child(Parent):    
    def __init__(self):
        self.name = "Lalith Raj R"
    def name_func(self):
        print("my name is lalith raj")     
        super().name_func()
               
obj = Child()
obj.name_func()


#---------Advance------------------

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
        print(self.price, self.brand)
class Information(Phone):
    def __init__(self, brand, color, price, os):
        super().__init__(brand, price)
        self.color = color
        print("completely submitted") 

obj = Information("Moto", "green", 26758, "Stock android")          
        