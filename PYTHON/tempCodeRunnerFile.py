def fact(lis,ind=0):
    if ind==len(lis):
        return
    print(lis[ind]) 
    return fact(lis,ind+1) 
 
    
li=[2,3,5,3,2,4,5]    
fact(li)  