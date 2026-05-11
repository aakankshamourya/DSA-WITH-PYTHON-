class Solution:
    def search(self, nums, target):
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
        return -1
print(Solution().search([-1,0,3,5,9,12],9))