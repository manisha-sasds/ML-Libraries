
# EVEN number 0 start, 10 en , 2 step
import numpy as np
print(np.arange(0,10,2))


# array fill diagonally

a=np.array([[22,78,45],[8,55,66],[8,55,66]])
np.fill_diagonal(a,3)
print(a)

# array full zeo

aa=np.array([[22,78,45],[8,55,66],[8,55,66]])
mm=np.full((3,3),0)
print(mm)


# Random function in numpy 
# 
import numpy as np
print(np.random.rand)

# 

from numpy import random
print(random.ran


aa=np.array([[22,78,45],[8,55,66],[8,55,66]])
mm=np.full((3,3),0)
print(mm)

# EVEN number 0 start, 10 en , 2 step
import numpy as np
# How to convert 2-D into flat array
lst=[[3,4,5],[8,9,66]]
print("\n list ",lst)
#  convert list to aarray here 
lst1=np.array(lst)
print(lst1)

# How to create this list into one d list using reshape



# compraewhat is the difference beteen array reshape n flattern


#  #  
arr=np.arange(12)
print("\n arr ",arr)

arr=np.arange(12).reshape(4,3)
print("\n arr ",arr)

arr=arr.ravel()
print("\n arr ",arr)
#  what is the difference between flattern n revel
arr=arr.flatten()
print("\n arr ",arr)

#  #  #  #  