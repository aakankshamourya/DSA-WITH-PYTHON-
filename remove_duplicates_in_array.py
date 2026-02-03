def dup_in_array(arr):
    n = len(arr)
    res = {}
    k = 0
    for i in range(n):
        res[arr[i]] = 0
    
    for j in res:
        arr[k] = j
        k += 1

    return k
print(dup_in_array([2,3,6,6,5,2,5,3]))
print(dup_in_array([1,1,1,1,1]))
    