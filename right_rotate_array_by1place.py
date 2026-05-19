def right_rptate_array_by1place(arr):
    n = len(arr)
    last_element = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr
print(right_rptate_array_by1place([1,2,3,4,5]))
print(right_rptate_array_by1place([10,20,30,40]))   



