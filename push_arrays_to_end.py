def push_arrays_to_end(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
    return arr
print(push_arrays_to_end([0,1,0,3,12]))


def push_arrays_to_end_two_pointer(arr):
    n=len(arr)
    left=0
    for right in range(n):
        if arr[right]!=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
    return arr  
print(push_arrays_to_end_two_pointer([0,1,0,3,12,0,4]))