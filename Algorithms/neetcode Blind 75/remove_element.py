def remove_element(arr, val):
    k =0
    for i in arr:
        if i!=val:
            arr[k]=i
            k+=1
    return k
print(remove_element([3,2,2,3], 3))