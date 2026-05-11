def search_insert_position(nums, target):
    n=len(nums)
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            left=mid+1
        else:
            right=mid-1
    return left
print(search_insert_position([1,3,5,6],5))
print(search_insert_position([1,3,5,6],2))