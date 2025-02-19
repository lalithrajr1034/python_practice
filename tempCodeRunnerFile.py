a=[1,2,34,54,7,6,38]
lis=[1,2,34,54,7,6,38]
lis.append(34)# adds an element at last [1, 2, 34, 54, 7, 6, 38, 34]
lis.sort()# set list in acending order [1, 2, 6, 7, 34, 34, 38, 54]
lis.sort(reverse=True)#set list in desending order [54, 38, 34, 34, 7, 6, 2, 1]
a.reverse()#it will reverse list [38, 6, 7, 54, 34, 2, 1]
a.insert(2     , 3000000)# it will insert 3000000 in index 2 
# insert(index , value  )  
print(lis)  
print(a)
