#Constructor is a special method that automatically execute when a object of a class is ctreated 
class constructor:
    def __init__(self,myname):#Self parameter is pointig towards object 
        self.name=myname #self = objectname.attribute

ob=constructor("hi")
print(ob.name)