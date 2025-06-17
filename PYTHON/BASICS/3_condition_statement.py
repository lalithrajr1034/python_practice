


# Python truthy and falsy values''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lis=[56,"45"]
if lis:# condition is True if list contains some element 
   print("it is not empty") 


# we can specify the the same kind of logic in many concepts  
"""
if "hello":   True (non-empty string)
if "":        False (empty string)
if [1, 2]:    True (non-empty list)
if []:        False (empty list)
if 0:         False (zero is false)
if 5:         True

"""
##.....................................................................................................


#if-elif-else

a=int(input("Enter the age="))
b=18
if(a<b):
    print("You are under age")

elif(a==b):
    print("You are now",a)    

else:
    print("You are adult")


##.....................................................................................................
 

#ternary operator condition statement    type-----1111
a=int(input("Enter Your Percentage:"))
print("You got Distinction") if a>=85 else print("You Didnt got Distinction")



#ternary operator condition statement    type-----2222
a=int(input("Enter first Number:"))
b=int(input("Enter Second Number:"))
val= 85 if a>b else 90
c=val+10
print(c)





