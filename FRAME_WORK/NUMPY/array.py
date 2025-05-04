
#------------------------this all will convesrt list as array-----------------
#(this is used whhen we have a list and we want to convert it to array)


#One dimension array
import numpy as np

Arr=np.array([2,3,4,45,6])
print(Arr)
   #or
import numpy as np
a=[2,3,4,6,7,8]
arr=np.array(a)
print(arr)   

#Multi dimensional array (matrix)
import numpy as np

mult_arr=np.array([[3,4,5,6],
                   [4,5,76,5]])
print(mult_arr)



#------------------------her we are creating array by default value -----------------
#To generate a full onse (or zeroes ,any number) in arrat=y

import numpy as np
#variable=np.zeroes(shape)      in shape for 1d (5) for 2d ((5,5))
zero_array=np.zeros((5,5))
print(zero_array)

#------------

import numpy as np
#variable=np.ones(shape)      in shape for 1d (5) for 2d ((5,5))
ones_array=np.ones((5,5))
print(ones_array)

import numpy as np
#variable=np.full(shape,value)     shape=1d (5) for 2d ((5,5)), value=any number
full_array=np.full((4,4),7)
print(full_array)

#----------------------crating sequence of number---------------

import numpy as np
#               arange(start,stop,step)
Arange_array=np.arange(0,    10,   1)
print(Arange_array)