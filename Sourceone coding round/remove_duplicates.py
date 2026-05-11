def remove_dup(arr):
    if not arr:
        return []
    j = 0

    for i in range(1, len(arr)):   # start from 1
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return arr[:j+1]


print(remove_dup([1,1,2,2,3,4]))