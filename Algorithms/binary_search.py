def binarySerach(arr,low,high,target):
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid,target
        elif arr[mid]>target:
            high=mid-1
        else:

            low=mid+1
    return -1,target
print(binarySerach([1,2,3,4,5,6,7,8,9],0,8,5))