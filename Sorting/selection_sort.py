def selection_sort(arr):
    n=len(arr)
    smallest_ele=arr[0]
    index=0
    for i in range(1,n):
        if arr[i]<smallest_ele:
            smallest_ele=arr[i]
            index=i
    return index
print(selection_sort([2,3,4,2,4,5,8,7]))
print(selection_sort([4,7,8,1,0,6]))



    