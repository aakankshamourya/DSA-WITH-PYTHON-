def single_non_duplicate(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if mid%2==1:
            
            mid-=1
        if arr[mid]==arr[mid+1]:
            left=mid+2
        else:
            right=mid
            
    return arr[left]
print(single_non_duplicate([1,1,2,3,3]))