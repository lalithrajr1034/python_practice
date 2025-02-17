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