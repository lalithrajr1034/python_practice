class Bank:
    def __init__(self):
        self.__paswrd = "lalithR77"
                
    def setter(self):
        changepass = input("Enter the new password")
        if (len(changepass) >= 6) and type == str:
            self.__paswrd = changepass
            
    def getter(self):
        return self.__paswrd        
        
obj = Bank()
obj.setter()
print(obj.getter())       
        