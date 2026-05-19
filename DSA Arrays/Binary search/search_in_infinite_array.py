def searchInInniteSortedArray(arr,target):
    low=0
    high=1
    while target>arr[high]:
        low=high
        high=high*2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1  
        else:
            low=mid+1
    return -1,target
print(searchInInniteSortedArray([1,2,3,4,5,6,7,8,9,10],5))               
print(searchInInniteSortedArray([23,67,79,100],67))