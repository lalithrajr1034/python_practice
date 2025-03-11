#Recursion:-
#       function calling itself repeteadly  

def recursion(b):
    if b==0: # base case  "This helps to stop the recursion"
        return
    print(b)
    recursion(b-1)
recursion(6)    










def factorial(n): 
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)  
num=int(input("Enter the factotial"))
print(f"Factorial of {num} is {factorial(num)}")#f-string