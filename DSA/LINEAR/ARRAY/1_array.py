# An array is the linear data structure which helps to store a similar type of data contagiously 


#Dis advantage
""" 1. Memory wastage (fixed size)   --> 
    2. Homogonous (lack of flexible) --> referencial array 
    3. Shifting (after deleting element we have to shift all element)
"""


import numpy as np
age=20
name=20
a = np.array(["li", "age", "name"])
print(a)

#--------------------------------------

#Referential array:
# This will store the adress of a array in a array //// compare to a array speed is low , and extra menory is used //// Python list is a referencial array
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
