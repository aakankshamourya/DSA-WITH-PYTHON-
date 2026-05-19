# Find the length of the longest subarray with at most two distinct elements (REDO)

nums = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

max_length = 0
my_dict = {}
left = 0
right = 0
n = len(nums)

while right < n:
    # Add current element to dictionary
    my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1

    # Shrink window if more than 2 distinct elements
    while len(my_dict) > 2:
        my_dict[nums[left]] -= 1
        if my_dict[nums[left]] == 0:
            del my_dict[nums[left]]
        left += 1

    # Update maximum length
    max_length = max(max_length, right - left + 1)

    right += 1

print(max_length)
