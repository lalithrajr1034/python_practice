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


#recurtion to print list
def fact(lis,ind=0):
    if ind==len(lis):
        return
    print(lis[ind]) 
    return fact(lis,ind+1) 
 
    
li=[2,3,5,3,2,4,5]    
fact(li)

