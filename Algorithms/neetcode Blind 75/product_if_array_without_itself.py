def productarrayWithoutItsel(arr):
    n=len(arr)
    result=[1]*len(arr)
    for i in range(n):
        prefix=1
        result[i]=prefix
        prefix*=arr[i]
    postfix=1
    for i in range(n):
        result[i]=postfix
        postfix*=arr[i]
    return result
print(productarrayWithoutItsel([1,2,3,4,6]))
        