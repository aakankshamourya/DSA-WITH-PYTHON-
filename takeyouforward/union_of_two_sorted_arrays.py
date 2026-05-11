def union_of_two_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union
if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    print(union_of_two_sorted_arrays(arr1, arr2))
    
    
def union_of_two_sorted_arrays_set(arr1, arr2):
    return sorted(set(arr1) | set(arr2))
if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6,9]
    arr2 = [2, 3, 5, 7]
    print(union_of_two_sorted_arrays_set(arr1, arr2))