def twosum(nums,target):
    res={}
    for i,n in enumerate(nums):
        r=target-nums[i]
        if r in res:
            return [res[r],i]
        res[n]=i    
print(twosum([2,7,11,15],9))  