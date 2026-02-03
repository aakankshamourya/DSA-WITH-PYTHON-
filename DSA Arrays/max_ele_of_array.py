def max_element(arr):
    max_ele=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_ele:
            max_ele=arr[i]
    return max_ele
print(max_element([1,2,3,430]))