def minimum_in_rotated_sorted_array(nums):
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid
    return nums[low]
print(minimum_in_rotated_sorted_array([1,2,3,-1,0]))


def minimum_times_array_is_rotated(nums):
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid
    return low
print(minimum_times_array_is_rotated([1,2,3,-1,0]))
print(minimum_times_array_is_rotated([4,5,0,1,2]))