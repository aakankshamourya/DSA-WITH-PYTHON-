def two_sum(nums,target):
    n=len(nums)
    
    for i in range(0,n-1):
         for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
        
        
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))



