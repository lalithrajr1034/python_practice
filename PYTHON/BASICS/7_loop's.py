# WHILE LOOP
 
ope1=1
no_loop=int(input("Enter the number of times to print: "))                         
while ope1<=no_loop:                               
# oper1 is a iterator ---------defination:( because it changes it's value for every loop)
# iteration -------------------defination:( it is a process of repeatin a set of instruction( or some task) until specific condition satisfy ) 
    print("I am Lalith")
    ope1+=1



#print numbers frm 1to 100 

min_num=1
while min_num<=100:
    print(min_num)
    min_num+=1



#print number from 100 to 1
    
iterator=100
while iterator>=1:
    print(iterator)
    iterator-=1


#Print a multiplication table of n
table=int(input("Enter Which table Should print:"))
max_val=int(input("Enter the number till the table should Execuite:"))    

iterator=0
while max_val>=iterator:
    tab= table *  iterator
    print(f"{table} x {iterator} = {tab}")
    iterator+=1



#print the element of the following list using a looop [1,4,9,16,25,36,49,64,81,100]

number=[1,4,9,16,25,36,49,64,81,100]
a=len(number)-1
iterator=0
while a>=iterator:
    print(number[iterator])
    iterator+=1
#                        (or)

number=[1,4,9,16,25,36,49,64,81,100]
b=["lal","SADAE","lal","SADAE","lal","SADAE","lal","SADAE","lal","SADAE",]
a=len(number)-1
iterator=0
while a>=iterator:
    print(number[iterator],b[iterator])
    iterator+=1

#search for a number x in this tupple using loop   (1,4,9,16,25,36,49,64,81,100)

number=(1,4,9,16,25,36,49,64,81,100)
a=len(number)
value=int(input())
i=0
while a>i:
    if (number[i]==value):
        print("Entered number",value,"Is found at index",i)   
    i+=1

# BREAK :-
    #It helps to brek the loop 


#CONTINUE:-
    #This key word helps skip that loop and move on to next
    
i=0
while i<=5:
    if i==3:
        i+=1
        continue #BY USING THIS WE SKIPED 3
    print(i)
    i+=1    


i=0
while i<=20:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1    







#FOR LOOP........................................................................................................................................

index=(1,2,3,4,5,6,7,8,9,9,3,54,56,67,78)
value=int(input("Enter the number:"))
i=0
for a in index:
    if a==value:
        print("I found this in index",i)
    i+=1    



#------>>> range

s=range(2,10,3)
for i in s:
    print(i)


   # (or)

for d in range(  2 ,    20 ,  2  ):   
#             start   stop   step
    print(d)



#------>>pass statement
# this statement does not do any thing it is used as a placeholder for feature code

for variable in range(10):
    pass
print("hi i am tejas")



#------->>to give spac or ,(coma) for every word

name="lalithraj"
for na in name:
    print(na,end=",")
        

print("hi lalith")


#to acess a loop elenect in a list we use a enumerate function
l=[2,5,42,2,54,7,78,4]
for i ,val in enumerate(l,1):
    print(f"index {i} value{val}")



def zeroshift(nums):
    current_element = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[current_element] = nums[current_element], nums[i]
            current_element += 1
    return nums

nums = [1, 0, 0, 2, 1, 0]
result = zeroshift(nums)
print(result)



#------------------------------------------------------------------------------------------------------------------------------------------
"""Advance"""
a = range(101)
b = range(100,201)
for a,b in zip(a,b):
    print(a,b)