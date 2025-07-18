class Demo:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

obj = Demo()

print(obj.public_var)      
print(obj._protected_var)  