class Main:
    def maths(self):
        print("Entered maths")
    def chemistry(self):
        print("Entered chemistry")
    def bio(self):
        print("Entered bio")
    def physics(self):
        print("Entered physics")        

subj=Main()
print(subj.chemistry())

#OUTPUT:
# Entered chemistry
# None  """(method itself doesn’t return anything, so by default, Python returns None)"""

#-------------------------------

class Main:
    def maths(self,TeacName):
        self.a=TeacName
        print("Entered maths")
    def chemistry(self):
        print("Entered chemistry")
    def bio(self):
        print("Entered bio")
    def physics(self):
        print("Entered physics")        
subj=Main()
subj.maths("Rudresh")
print(subj.a)

