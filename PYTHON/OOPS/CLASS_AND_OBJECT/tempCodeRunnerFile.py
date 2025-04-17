
class Atm:
    def __init__(self):
        self.balance=0
        self.pin=""
        self.main()  #by using this did not required to call a method
        
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
            self.create_pin()
        elif input_option==2:
            pass  
        elif input_option==3:
            pass
        elif input_option==4:
            pass  
        elif input_option==5:
            pass  
         
    def create_pin(self):
            input_pin1=input("Enter a pin ")
            input_pin2=input("Re-Enter a pin ")
            if input_pin1==input_pin2:
                print("Entered pin id is sucessfully set")
                self.main()
            else:
                print("Entered pin dose not matched\n\t\tStarting from first\n.....................................\n\n")
                val=1
                self.main()
           
                

obj=Atm()   
