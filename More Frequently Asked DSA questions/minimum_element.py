def min_element(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
    return arr[low]
print(min_element([3,4,5,1,2]))