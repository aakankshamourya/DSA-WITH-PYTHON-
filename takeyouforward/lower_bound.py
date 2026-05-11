class Solution:
    def lowerBound(self, nums, x):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<x:
                left=mid+1
            else:
                right=mid-1
        return left
print(Solution().lowerBound([1,2,3,4,5],3))


class Solution:
    def lowerBound1(self, nums, x):
        left=0
        right=len(nums)-1
        ans=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
print(Solution().lowerBound1([1,2,3,4,5],3))
