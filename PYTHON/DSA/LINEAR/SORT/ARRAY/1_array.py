# An array is the linear data structure which helps to store a similar type of data


import numpy as np
age=20
name=20
a = np.array(["li", "age", "name"])
print(a)

#--------------------------------------
#Referential array:
import numpy as np 
li1=[3,5]
li2=["lal","lalith"]

# full=[li1,li2]
a=np.array([1,"li"])
print(li1,li2)
print(a)


#--------------------------------------
#Dynamic array
#A dynamic array allows to Store elements in a contiguous block of memory But also increase and decrease in size automatically when needed

def listt():
    l=[]
    size=10
    for index in range(0,size):
        l[index]
        if index==size-2:
            size =size+100

    print(size)
listt()    