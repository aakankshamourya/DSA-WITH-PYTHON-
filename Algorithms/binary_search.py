def binary_search(arr, target):
    """Return the index of target in a sorted list arr, or -1 if not found."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = binary_search(data, target)
    print(f"Target {target} found at index: {index}" if index != -1 else f"Target {target} not found")
