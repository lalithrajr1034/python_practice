#here i created my own datatype 


#OUTPUT 2.857142857142857
# here while printing a it will show a fraction(2.857142857142857) we want to store same as 20/7



class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator 
        self.denominator=denominator
        
        #This __str__ will automatically execute when the clas of the object is kept inside the print function  
    def __str__(self): #__str__ (magic method) it will activate when print function is called
        return "{}/{}".format(self.numerator,self.denominator)
        # or this both line are same called string formating
        # return f"{self.numerator}/{self.denominator}"
                                                                                 
    def __add__(sel,other): #obj1.__add__(obj2)
        #here paramater is work same as the self but forst obj1 goes to "sel" and obj2 goes to "other"
        temp1=sel.numerator*other.denominator+sel.denominator*other.numerator
        temp2=sel.denominator*other.numerator+sel.numerator*other.denominator
        return f"{temp1}/{temp2}"
obj1=Fraction(7,8) #creating object
obj2=Fraction(5,7)
print(obj1*obj2)

