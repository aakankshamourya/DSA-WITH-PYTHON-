def maxproduct(arr):
    res=arr[0]
    n=len(arr)
    for i in range(n):
        currproduct=1
        for j in range(i,n):
            currproduct*=arr[j]
            res=max(res,currproduct)
    return res
print(maxproduct([2,3,-2,4,7,3]))