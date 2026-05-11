def reverse_array(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
print(reverse_array([1,2,3,4,5]))