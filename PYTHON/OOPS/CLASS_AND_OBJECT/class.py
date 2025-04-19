#...................CLASS................................

# Data          +   Functions   =  Class
# Attributes        Methods       
# Property          Behavior

#Data :-  like discription about the element (ex: colour, wheels , brand)
#Function:-it is like a behaviour of the element (ex: calculate , Show milage)

#NOTE :- class name should be in pascal case = ThisIsPascalCase
#NOTE :- Function(or Method) should be in snake case = this_is_snake_case

#instance variable:

class lalith:
    a="allalal"    
    def hi():
        print("hello")
lal=lalith()       
print(lal)  




#---------------Code with harry -----------------

class college:
    inc=4      # class variable
    def __init__(self,branch,sem):
        self.a=branch # instance variable
        self.b=sem    # instance variable
    def nextsem(self):
        self.b=self.b*college.inc    


lalith=college("AI",4)
lalith.nextsem()
print(lalith.b)

#--------------------

class lalith:
    add=1  #Class variable 
    def __init__(self,name,age):
        self.nam=name #Instance variable 
        self.age=age  #Instance variable
    def raj(self):
        self.age+=lalith.add  #  (lalith.add) it will directly check to class variable, (or self.add) if we use self it will check instance variable then it will check class variable
obj=lalith("lalith",19)        
obj.raj()
print(obj.age)