## REDO SEARCH IN ROTATED SORTED ARRAY

def search_in_rotated_sorted_array(arr, target):           
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
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

    return -1
print(search_in_rotated_sorted_array([4,5,6,7,0,1,2],0))