# CLASS

# Data          +   Functions   =  Class
# Attributes        Methods       
# Property          Behavior

#Data :-  like discription about the element (ex: colour, wheels , brand)
#Function:-it is like a behaviour of the element (ex: calculate , Show milage)

#NOTE :- class name should be in pascal case = ThisIsPascalCase
#NOTE :- Function should be in snake case = this_is_snake_case

class lalith:
    a="allalal"    
    def hi():
        print("hello")
lal=lalith()       
print(lal)  

#...................................
#CONSTRUCTOR(__init__())
#Constructor is a special method that automatically execute when a object of a class is ctreated 
class constructor:
    def __init__(self,myname):#Self parameter is pointig towards object 
        self.name=myname #self = objectname.attribute

ob=constructor()
print(constructor.name)



class l:
    def __init__(self):
        print()
    def lalith(self):
        self.a=4
        print(a)
l.lalith()        