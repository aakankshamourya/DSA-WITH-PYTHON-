def twoSum(nums,target):
    res={}
    for i,n in enumerate(nums):
        r =target-nums[i]
        if r in res:
            return [res[r],i]
        res[n]=i
print(twoSum([1,2,3,4],7))