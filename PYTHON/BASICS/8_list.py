#It is a predefine data type that helps to store a set of value's

ind=[67,76,45,78]
print(ind[-1])

#changing element(it is possible only in list but not in strings)
 
ind=[67,76,45,78]
print(max(ind))

ind[1]=3
print(ind)   #replace 76 by 3 output is [67, 3, 45, 78]


#---------------- slicing -------- list_name[start:stop:step]---

#it is possible in list also 

a=[1,23,4,6,7,65]
# a[Start_index : Ending_index]
c=a[ 1          :            4]
print(c) #output is [23, 4, 6]





#-------------------List method------
a=[1,2,34,54,7,6,38]
lis=[1,2,34,54,7,6,38]
lis.append(34)# adds an element at last [1, 2, 34, 54, 7, 6, 38, 34]
lis.sort()# set list in acending order [1, 2, 6, 7, 34, 34, 38, 54]
lis.sort(reverse=True)#set list in desending order [54, 38, 34, 34, 7, 6, 2, 1]
a.reverse()#it will reverse list [38, 6, 7, 54, 34, 2, 1]
a.insert(2     , 3000000)# it will insert 3000000 in index 2 output is [38, 6, 3000000, 7, 54, 34, 2, 1]
# insert(index , value  )  
a.remove(1)#removes a 1 if 1 is multiple then removes first element of same kind
a.pop(3)#removes a 3rd index element
print(lis)  
print(a)



#------------------TOUPLES----------

#Touple are the immutable, and used to store the elements in paranthesis()

c=input()
a=(2,3,4,5,6,7,3,"m")
l={23,"ds",23,"df"}
print(a.index(c))#helps to find the index of element
print(a.count(c))#helps to find the how many same type of elements are presnt

                                                                                                                                                        