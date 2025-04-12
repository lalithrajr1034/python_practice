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