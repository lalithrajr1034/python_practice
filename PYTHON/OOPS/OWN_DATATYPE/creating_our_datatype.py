#here i created my own datatype 


#OUTPUT 2.857142857142857
# here while printing a it will show a fraction(2.857142857142857) we want to store same as 20/7



class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator 
        self.denominator=denominator

    def __str__(self): #__str__ (magic method) it will activate when print function is called
        return "{}/{}".format(self.numerator,self.denominator)
        
