def even_more_odd(arr):
    for i in range(1, len(arr)):
        if i % 2 == 1:  # odd index
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        else:  # even index
            if arr[i] > arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

print(even_more_odd([1, 3, 2, 2, 5]))

    
    