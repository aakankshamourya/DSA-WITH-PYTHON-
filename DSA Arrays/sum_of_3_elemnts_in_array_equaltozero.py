def trio(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    count+=1
    return count
print(trio([0,-1,2,-3,1]))




######################################################################################################

nums = [-1,0,1,2,-1,-4]
nums.sort()
i = 0
n = len(nums)
ans = set()
for i in range(n):
    j = i+1
    k = len(nums)-1
    while j<k:
        s=nums[i] + nums[j] + nums[k] 
        if s==0:
            ans.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
        elif s>0:
            k-=1
        else: j+=1

print(list(ans))       
    