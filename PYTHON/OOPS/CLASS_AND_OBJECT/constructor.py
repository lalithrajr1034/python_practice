#........................CONSTRUCTOR(__init__())..........................

#Constructor is a special method that automatically execute when a object of a class is ctreated 
class constructor:
    def __init__(self,myname):#Self parameter is pointig towards object 
        self.name=myname #self = objectname.attribute

ob=constructor()
print(constructor.name)



class name:

# This is constructor
    def __init__(self):
        print("This is constructor")
# this is paramaterised constructor(in this constructor we passed "nam" as a parameter except self)
    def __init__(self,nam):
        self.a=nam

obj=name("Nithin")
print(obj.a)
