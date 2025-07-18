# Geter and Setter are the methods used to secure data from direct acess of a private and proteted data by creating a method inside a class
# Getter: method that returns the value of a private and protected
# Setter: method that we set or updates the value of protected and private 

class Bank:
    def __init__(self):
        self.__paswrd = "lalithR77"
                
    def setter(self):
        changepass = input("Enter the new password")
        if (len(changepass) >= 6) and type(changepass) == str:
            self.__paswrd = changepass
        else:
            print("Error")   
    def getter(self):
        return self.__paswrd        
        
obj = Bank()
obj.setter()
print(obj.getter())       
        