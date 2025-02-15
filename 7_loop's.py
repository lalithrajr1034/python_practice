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
