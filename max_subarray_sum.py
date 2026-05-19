def maxsubarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        currSum=0
        for j in range(i,len(arr)):
            currSum+=arr[j]
            res=max(res,currSum)
    return res
print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))
    