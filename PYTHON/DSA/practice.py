#Time complacity:
    #It is calculating a mathematical expresion for increse in time taken to execute a program w r s to incresing in no of input



l=[1,2,3,4,5]
for i in range(0,len(l)//2):
    other=len(l)-1-i
    temp=l[i]        #if we remove this it will be  and replace temp by l[i]  [5, 4, 3, 4, 5]
    l[i]=l[other]
    l[other]=temp    #if we replace temp with l[i] and past it above 10 and it will be [1, 2, 3, 2, 1]
print(l)


l=[1,2,3,4,5]
le=len(l)-1
for i in range(le,-1,-1):
    le=len(l)
    new_list=le-1-i
    l[i]=l[new_list]
