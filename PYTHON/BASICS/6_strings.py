# it is a data type which helps us to store a sequence of charactor 


oper1='abcd'
oper2="abcd"
oper3="""abcd"""

# a='hi lalithraj i am seena's friend'                                          ((to avoid this ve want to see the comas that we are using))  
a="hi lalithraj i am seena's friend" #solution


#i think 
""" this method is best use for string  """



# escape sequence charactor
char1="hi i am lalith\traj \n i am just 18"
print(char1)
      #(or)
print("hi i am lalith\traj \n i am just 18")      
 


#string concatination(adding two or more strings)

a="suraj"
b="seena"
c="teja"
d="nithin"
print(f"{a} {b} {c} {d}")


#string length(Helps to define a length of a string)

a="suraj"
print(len(a))#this helps to define the length of the numbers





#------------INDEXING------------

#This indexing is says that each element is acessed by the index value
#there are types in indexing
   #positive indexing (index value of Starting element is 0 and index value of second element 1)
   #negitive indexing (index value of last element is -1 and index value of last second element -2)
   #2-dimensional (or) multidimensional indexing

a="asdfghjkl" #index value are[0,1,2,3,4,5,6,7,8]
print(a[1]) # + ve indexing


a="asdfghjkl" #index value are[-9,-8,-7,-6,-5,-3,-2,-1]
print(a[1]) # - ve indexing



matrix=[[1,2,3], #index value are 0 1 2
        [5,6,7],                 #1 
        [8,7,4]                  #2
      ]
print(matrix[0][0])  






#---------Slicing---------
# slicing is acessing part ot the string
#in this slicing also we can acess in -ve indexing
#(in this also ending index is not included but starting index is going to execute)

var="nithintejas"
print(var[1:4]) #index 1 is inclusive and index 4 isexclusive

#   other technique(or)

var="nithintejas"
print(var[3:len(var)])

# in this case by default value will set 

print(var[:3])#default value is 0
print(var[3:])#default value is len(var)





#-----------------Functions------------------------------------------


val="i am lalith raj studying in MIT mysore"
print(val.capitalize()) #out put is  I am lalith raj studying in mit mysore
print(val.endswith("e")) #out put is True
print(val.replace("i","a")) #out put is a am lalath raj studyang an MIT mysore
print(val.find("lalith")) #out put is 5
print(val.count("i")) #out put is 4
# actual string is not changed
print(val)



# so to manupulate the string

val="i am lalith raj $studying in MIT mysore"  
val=val.replace("i","a")
print(val)


#write a porgram to find a palandrome(EX:-malayalam) 

a=[1,2,3,4,3,2,1]
b=[1,2,3,4,3,2,1]
b.reverse()
if a==b:
    print ("value are palindromy")
else:
    print("elements are not palindromy")    
    



#string method------------------


str="lalit-raj-r,r,raj"
fname,mname,lname=str.split(",")
print(fname)    