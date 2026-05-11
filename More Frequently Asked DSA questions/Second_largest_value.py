def second_largest(arr):
    first=-10**9
    second=-10**9
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]
    return second
print(second_largest([1,2,4,7,8,9,11,18]))