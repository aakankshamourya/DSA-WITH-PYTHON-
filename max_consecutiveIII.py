def longest_ones(nums, k):
    left = 0
    right = 0
    zeros = 0
    max_len = 0
    n = len(nums)

    while right < n:
        # expand window
        if nums[right] == 0:
            zeros += 1

        # shrink window if zeros exceed k
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # update maximum window size
        max_len = max(max_len, right - left + 1)

        right += 1

    return max_len
print(longest_ones([1,1,1,0,0,0,1,1,1,1,0],2))