def highest_in_neighbours(arr):
    l=0
    r=len(arr)-1
    for i in range(len(arr)-1):
        mid=(l+r)//2
        if arr[mid]>arr[i+1]or arr[mid]>arr[i-1]:
            r=mid-1
            return arr[mid]
           
        elif arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            return arr[i]   
        elif arr[i+1]>arr[i] and arr[i+1]>arr[i+2]:
            return arr[i+1]
        else:
            l=mid+1
    return -1
print(highest_in_neighbours([1,2,3,5,4,3,1,2]))