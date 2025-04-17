class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator 
        self.denominator=denominator

        def __str__(self): #__str__ (magic method) it will activate when print function is called
            return "{}/{}".format(self.numerator,self.denominator)
        
obj=Fraction(7,8) #creating object

print(obj)