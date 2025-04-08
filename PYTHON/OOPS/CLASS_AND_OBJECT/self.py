#...........................SELF.................................
# RULES 
#In a class there are somany methods, in there each of them can't acess(TO ACESS THAT WEHAVE USE OBJECT in the form of "SELF")

class School:
    def __init__(self):
        print("Hi lalih")
    def artificial_inteligence(self):
        self.a=3
        print("This is class")

School.artificial_inteligence()