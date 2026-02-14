def minimum_in_rotated_sorted_array(arr):
    l = 0
    r = len(arr) - 1
    min_ele = float('inf')
    while l <= r:
        if arr[l] <= arr[r]:
            min_ele = min(min_ele, arr[l])
            break
        mid = (l + r) // 2
        min_ele = min(min_ele, arr[mid])
        if arr[l] <= arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return min_ele

print(minimum_in_rotated_sorted_array([4,5,6,1,2,3]))

            