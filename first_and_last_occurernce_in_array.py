def first_occurrence(arr, target):
    low=0
    high=len(arr)-1
    lb=-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
print(first_occurrence([1,2,2,2,3,4,5],2))

############################################################

def last_occurrence(arr, target):
    low=0
    high=len(arr)-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            ub=mid
            low=mid+1
        else:
            high=mid-1
    return ub
print(last_occurrence([1,2,2,2,3,4,5],2))


########################################################################333


def top_last_occurrence(arr,target):     ########### wrong logic review later
    low=0
    high=len(arr)-1
    lb=-1
    ub=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            if arr[mid]==target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        elif arr[mid]<=target:
            if arr[mid]==target:
                ub=mid
                low=mid+1
            else:
                high=mid-1  
    return (lb,ub)
print(top_last_occurrence([1,2,2,2,3,4,5],2))