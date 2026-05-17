def concatenation_array(arr1,arr2):
    conct=arr1+arr2
    return conct
print(concatenation_array([1,2,3,4],[6,7,8,9]))

def concat_array(arr1,arr2):
    arr1.extend(arr2)
    return arr1
print(concat_array([6,7,8,9],[0,1,2,4]))

import numpy as np
arr1=[1,2,3,4,5,6,7]
arr2=[6,7,8,9,0,6]
res=np.concatenate((arr1,arr2))
print(res)