# CLASS

# Data          +   Functions   =  Class
# Attributes        Methods       
# Property          Behavior

#Data :-  like discription about the element (ex: colour, wheels , brand)
#Function:-it is like a behaviour of the element (ex: calculate , Show milage)

#NOTE :- class name should be in pascal case = ThisIsPascalCase
#NOTE :- Function(or Method) should be in snake case = this_is_snake_case

class lalith:
    a="allalal"    
    def hi():
        print("hello")
lal=lalith()       
print(lal)  

#OBJECT............................
#object is a instance of class
#instance==A class is like a recipe""An object is the cake made using that recipe""That cake is an instance of the recipe (class)."""
#In every time while creating a object it will occupy different location

class School:
    def __init__(self):
        print("Hi lalih")
    def artificial_inteligence(self):
        self.a=3
        print("This is class")

School.artificial_inteligence()#THis is an object



#...................................
#CONSTRUCTOR(__init__())
#Constructor is a special method that automatically execute when a object of a class is ctreated 
class constructor:
    def __init__(self,myname):#Self parameter is pointig towards object 
        self.name=myname #self = objectname.attribute

ob=constructor()
print(constructor.name)


#______________________

class name:

# This is constructor
    def __init__(self):
        print("This is constructor")
# this is paramaterised constructor(in this constructor we passed "nam" as a parameter except self)
    def __init__(self,nam):
        self.a=nam

obj=name("Nithin")
print(obj.a)


# RULES 
#In a class there are somany methods, in there each of them can't acess(TO ACESS THAT WEHAVE USE OBJECT in the form of "SELF")

class School:
    def __init__(self):
        print("Hi lalih")
    def artificial_inteligence(self):
        self.a=3
        print("This is class")

School.artificial_inteligence()