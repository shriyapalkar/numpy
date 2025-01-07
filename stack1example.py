import numpy as np
arr1=np.array([5,6,7])
arr2=np.array([6,7,8])

## Using np.stack() function to stack two arrays column-wise:
arraycompiled=np.stack((arr1,arr2),axis=0)
print(arraycompiled)