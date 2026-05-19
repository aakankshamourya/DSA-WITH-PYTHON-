def maxprodexpself(arr):
    n = len(arr)
    for i in range(n):
        res=[1]*n
        for j in range(n):
            if i!=j:
                res[i]*=arr[j]
    return max(res)
print(maxprodexpself([1,2,3,0,8]))
print(maxprodexpself([2,3,4,5]))