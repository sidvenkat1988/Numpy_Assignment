#Problem 1
#Replacing odd numbers in an array with -1
import numpy as np
#Method 1
arr = np.array([0,1,2,3,4,5,6,7,8,9])
for i in arr:
    if arr[i]%2 != 0:
        arr[i] = -1
arr


#Method 2 (Reference : https://stackoverflow.com/questions/10335090/numpy-replace-negative-values-in-array)
arr        
arr[arr%2 != 0] = -1
arr