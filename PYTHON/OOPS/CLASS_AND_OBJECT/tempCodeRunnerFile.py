class lalith:
    add=1
    def __init__(self,name,age):
        self.nam=name
        self.age=age
    def raj(self):
        self.age+=lalith.add    
obj=lalith("lalith",19)        
obj.raj()
print(obj.age)