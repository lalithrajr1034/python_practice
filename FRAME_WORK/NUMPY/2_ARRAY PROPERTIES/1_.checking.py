#This concepts are related to checking

#This include----> shape, size, ndim, dtype

#to check the size
import numpy as np
a=np.array([[2,3,5,6],[3,45,6,7]])
print(a.size)# output 8


#to check the shape
import numpy as np
a=np.array([[2,3,5,6],[3,45,6,7]])
print(a.shape)# output(2, 4)

#To check 1d, 2d, or 3d (ndim)=numbr of dimension 
import numpy as np
a=np.array([2,3,5,6])
b=np.array([[2,3,5,6],[3,45,6,7]])
c=np.array([[[2,3,5,6],[3,45,6,7]]])
print(a.ndim,b.ndim,c.ndim)

#To check the data type (dtype)=data type
import numpy as np
a=np.array([[2,3,5,6],[2,3,5,6]])
print(a.dtype)

