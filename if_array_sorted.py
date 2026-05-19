def is_sorted(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True
print(is_sorted([1,2,3,4,5]))
print(is_sorted([2,3,6,1,2]))