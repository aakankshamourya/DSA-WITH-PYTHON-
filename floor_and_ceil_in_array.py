def floor_ceil(arr,target):
    low=0
    high=len(arr)-1
    floor=-1
    ceil=-1

    for i in range(len(arr)):
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                floor=arr[mid]
                ceil=arr[mid]
            else:
                if arr[mid]<target:
                    floor=arr[mid]
                    low=mid+1
                else:
                    ceil=arr[mid]
                    high=mid-1
                return (floor,ceil)
print(floor_ceil([1,2,4,6,8],5))