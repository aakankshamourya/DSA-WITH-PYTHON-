def floor_and_ceil(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    floor = -1
    ceil = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return nums[mid], nums[mid]

        elif nums[mid] < target:
            floor = nums[mid]
            left = mid + 1

        else:
            ceil = nums[mid]
            right = mid - 1

    return floor, ceil
print(floor_and_ceil([1, 2, 3, 4, 5], 3))
print(floor_and_ceil([1, 2, 3, 4, 5], 0))