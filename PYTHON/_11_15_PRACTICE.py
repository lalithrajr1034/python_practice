
##FUNCTION
#Write a function to print the length of a list 

lis=[2,3,4,5,6,8,9,7]
def lengt_of_list(lis):
    print(len(lis))
lengt_of_list()       

     #OR

num=[2,3,4,5,6,8,9,7]
def lengt_of_list(list):
    print(len(list))

lengt_of_list(num)


#write a function to print the element of a list in a single line
lis=[2,34,5,6,78,8,8,90]
def list_s():
    print(lis)
list_s()    
      #OR
lis=[2,34,5,6,78,8,8,90]
def list_s(list):
    print(list)
list_s(lis)    


#Write a function to find the factorial of n

def factorial(numb):
    fact = 1  
    while numb > 1:
        fact *= numb  
        numb -= 1  
    return fact  


num = int(input())
print(factorial(num))

def my_func(nu):
    if nu%2==0:
        print("ODD")
    else:
        print("EVEN")    

a=int(input())
my_func(a)


#Recursion problem
#Write a recursive function to calculate the sum of first n natutal numbers 
def sum(inpu):
    if inpu==1:
        return 1
    return sum(inpu-1) + inpu

na=int(input())
g=sum(na)
print(g)    