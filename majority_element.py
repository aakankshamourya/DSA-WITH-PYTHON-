def majority_element(nums):
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[i]==nums[j]:
                count+=1
        if count>n//2:
            return nums[i]
    return -1
print(majority_element([3,2,3]))