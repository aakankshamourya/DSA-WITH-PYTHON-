def search_in_array(arr, target):
    n=len(arr)
    high=n-1
    low=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(search_in_array([1,2,3,4,5],3))
print(search_in_array([10,20,30,40,50],25))