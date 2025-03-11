#Recursion:-
#       function calling itself repeteadly  

def recursion(b):
    if b==0: # base case  "This helps to stop the recursion"
        return 0
    print(b)
    recursion(b-1)

recursion(6)    


#recursion through factorial

def factorial(n): 
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)            # n!=(n-1)!*n
    
num=int(input("Enter the factotial"))
print(f"Factorial of {num} is {factorial(num)}")#f-string