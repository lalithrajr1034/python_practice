#LOOPS

# print number from 1 to 100

for data in range(1 , 101 , 1):
    print(data)



# print number from 100 to 1  
a=range(100)
ran=len(a)
num=1                            
while ran>=num:                      # in while loop
    print(ran)
    ran-=1

# print number from 100 to 1  

for variable in range(100 , 0 ,-1):  # in for loop
    print(variable)     


# print multiplication table of n

n=int(input("Enter the table:"))
rra=int(input("Enter the length of the table:"))
ra=rra+1
for a in range(1,ra):
    c=a*n
    print(f"{n}x{a}={c}")   

# Write a Python program that takes an integer input from the user and checks whether 
# it is odd or even. If the number is even, print "Even", otherwise print "Odd"   

inp=int(input("Enter a integer:"))

if inp%2==0:    
    print("Even")   
else:
    print("Odd")     

# Write a Python program that prints all numbers from 1 to 100 that are divisible by both 3 and 5

val=range(1,101,1)
for num in val:
    if num%3==0 and num%5==0:
        print(num)
        continue

# Write a Python program that continuously takes user input (numbers) and adds them to a total sum.
# The program should stop when the user enters a negative number and then print the sum of all 
# positive numbers entered      

a=0
while True:
    inpu=int(input())
    if inpu<0:
        break
    a=a+inpu

print("Sum of all +ve numbers",a)


# Write a Python program that takes a number as input from the user and checks whether the number is a prime number.
#  A prime number is only divisible by 1 and itself
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2:
    print(f"{num} is a prime number.")
elif num % 2 == 0:
    print(f"{num} is not a prime number.")
elif num == 3:
    print(f"{num} is a prime number.")
elif num % 3 == 0:
    print(f"{num} is not a prime number.")
else:
    print(f"{num} is a prime number.")






