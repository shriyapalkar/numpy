import numpy as np
arr = np.array(['a', '2', '3'], dtype='i')

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

import numpy as np
arr = np.array([1.6,3.4,5.6,7.8])
print(arr.dtype)
arr1 =arr.astype('i')
print(arr1)
print(arr1.dtype)