def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
print(lower_bound([1, 2, 4, 4, 5], 4))

########################################################################################################

def upper_bound(arr, target):
    low=0
    high=len(arr)
    while low<high:
        mid=(low+high)//2
        if arr[mid]<=target:
            low=mid+1
        else:
            high=mid   
    return low
print(upper_bound([1, 2, 4, 4, 5], 4))