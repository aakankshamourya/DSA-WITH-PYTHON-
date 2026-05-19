def thirdlargest(arr):
    n=len(arr)
    first=-1
    second=-1
    third=-1
    for i in range(n):
        if arr[i]>first and arr[i]!=second:
            first=arr[i]
    for i in range(n):
        if arr[i]>second and arr[i]!=first:
            second=arr[i]
    for i in range(n):
        if arr[i]>third and arr[i]!=first and arr[i]!=second:
            third=arr[i]
    return third
print(thirdlargest([2,3,6,6,5]))