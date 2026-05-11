def min_in_rotated_sorted(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]>arr[right]:
            left=mid+1
            
        else:
            right=mid
    return arr[left]
print(min_in_rotated_sorted([3,4,5,1,2]))
print(min_in_rotated_sorted([7,8,9,0,1,2,3,4,5,6]))