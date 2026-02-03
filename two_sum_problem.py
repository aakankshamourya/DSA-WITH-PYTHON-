def two_sum(nums,target):
    num_map={}
    for i in range(len(nums)):
        complement=target - nums[i]
        if complement in num_map:
            return [num_map[complement],i]
        num_map[nums[i]]=i
    return []
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))