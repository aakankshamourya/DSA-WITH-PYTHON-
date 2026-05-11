def remove_dup(arr):
    res=[]
    for i in range(len(arr)):
        if arr[i] not in res:
            res.append(arr[i])
    return res
print(remove_dup([1,1,2,2,3,4]))