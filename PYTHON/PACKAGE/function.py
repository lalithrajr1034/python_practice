# main is mainpy class 
           
class mainpy:    
    def __init__(self):
        self.atm = Atm()  # Create an object of Atm class
        self.main()
    def main(self):
        
        user_input="""
                   hello how are you 
                   1 Enter to create a pin
                   2 Enter to deposit money
                   3 Enter to withdraw
                   4 Enter to check balance
                   5 Enter to exit
                   """
        print(user_input)
        input_option=int(input("Enter your choice "))

        if input_option==1:
            self.atm.create_pin()
        elif input_option==2:
            self.atm.depost_money() 
        elif input_option==3:
            pass
        elif input_option==4:
            pass  
        elif input_option==5:
            print("Thank you for using ATM. Bye! 👋")
            
        else:
            print("Invalid choice. Try again.")
        
class Atm:
    def __init__(self):
        self.balance=0
        self.pin=int(input("Enter a pin "))
        self.main=mainpy      #object
        
    def create_pin(self):
            self.pin=input("Enter a pin ")
            if True:
                print("Entered pin id is sucessfully set\n")
                self.main()
                
    def depost_money(self):
           self.deposit_pin=input("Enter the pin to deposit money ")
           
           if self.deposit_pin==self.pin:
               deposit_money=int(input("Enter the amount to be deposited "))
               print(f"Your current balence amount {deposit_money}")
               self.main()
           else:
               print("You entered wrong password")
               self.withdraw_money() 

    def withdraw_money(self):
         pass
    def check_balance(self):
         pass           
               


