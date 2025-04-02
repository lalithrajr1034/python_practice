# write a program to input 2 number and print their sum
opera1=int(input("Enter First Number:"))
opera2=int(input("Enter second number:"))
sum=opera1+opera2
print("Solution is",sum)



#area of square

opera1=int(input("Enter size of side:"))
sum=opera1**2
print("Solution is:",sum)


#average of 2 f;oting number

opera1=float(input("Enter first floting number:"))
opera2=float(input("Enter second floting number:"))
avg=(opera2+opera1)/2
print(avg)

# print true if a>=b else print false
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("True") if a>=b else print("False")

#            (or)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a>=b)



inpu=int(input())
i=1
while inpu >=i:
    st=str(i)
    print(st)
    i+=1
    print(len(st))


# Write a program that checks whether a number is positive, negative, or zero    

number=int(input("Enter your number "))
if number==0:
    print("you entered zero")
else:    
    print("-ve")if number<0  else print("+ve")
     

     