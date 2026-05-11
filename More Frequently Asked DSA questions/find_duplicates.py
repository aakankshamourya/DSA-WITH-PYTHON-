def find_dup(arr):
    seen=set()
    duplicates=set()
    for i in range(len(arr)):
        if arr[i] in seen:
            duplicates.add(arr[i])
        else:
            seen.add(arr[i])
    return list(duplicates)
print(find_dup([1,2,3,4,5,2,3]))