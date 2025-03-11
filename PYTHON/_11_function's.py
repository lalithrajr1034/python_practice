#it is a block of code which helps to avoid Redundent(repeat) a code again and again 

def lal():#def-->Key word
    print("a")


lal() #Calling the function
#...................................................................
#example  1
def la(a,b,c):
    sum=(a+b+c)/3
    return sum
print(la(2,3,5))

#example 2
def la(a,b,c):
    sum=(a+b+c)/3
    print(sum)
    return sum
la(2,3,5)

#default of parameter...............................................

def lal(a=2,b=3): #parametres (a,b=4) but this is error(a=2,b)
    print(a*b)
lal()     #arguments tested (b=5),1 and (3,5)

#...................................................................

#PRACTICE QUESTIONS
#Write a function factorial(n) that returns the factorial of a number using recursion

def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

n = int(input())
print(factorial(n))
