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

for variable in range(100 , 0 ,-1):  # in  for loop
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


#Finding the runner(second largest element) in list




list=[2,3,6,6,5]

list.sort(reverse=True)
n=1
while n<len(list) and list[0]==list[n]:
    n+=1

if n<len(list):
    print(list[n])


#Write a program that takes a list of numbers as input and prints all even numbers. If the list contains no even numbers, print "No even numbers found."
    
a = [1, 3,  5,  7,  9]
i = 0
c = len(a)
found_even = True  
while i < c:
    if a[i] % 2 == 0:
        print("Even number:", a[i])
        found_even = False
    i += 1

if found_even:
    print("No even numbers found.")
   
   
#2. Loops + Dictionary (Take a string as input and count the occurrences of each character using a dictionary. Print the dictionary after counting)




#loops  test

lalith=int(input("Enter the number"))

for nam in range(2,lalith):
    print(f"hi{nam} * {lalith}")


s="lkfhiureybnjk"
d=[2,3,4]
b={"key":"value"}
c=(2,34,4,s,d,b)
print(c)

a=int(input())
b=int(input())
e=int(input())
d=pow(a,b)
print(d)
c=pow(a,b,e)
print(c)