class Solution:
    
    def isPossible(self, nums, mid, target):

        current_sum = 0

        # First window
        for i in range(mid):
            current_sum += nums[i]

        if current_sum >= target:
            return True

        # Sliding window
        for i in range(mid, len(nums)):

            current_sum += nums[i]
            current_sum -= nums[i - mid]

            if current_sum >= target:
                return True

        return False


    def minSubArrayLen(self, target, nums):

        ans = float('inf')

        left = 1
        right = len(nums)

        while left <= right:

            mid = (left + right) // 2

            if self.isPossible(nums, mid, target):

                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return 0 if ans == float('inf') else ans


# Example
obj = Solution()

print(obj.minSubArrayLen(7, [2,3,1,2,4,3]))