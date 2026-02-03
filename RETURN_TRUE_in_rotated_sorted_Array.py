def rotated_sorted_array_return_true(arr, target):           
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
print(rotated_sorted_array_return_true([4,5,6,7,0,1,2],0))