def reverse_array(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
print(reverse_array([1,2,3,4,5]))


def reverse_array_recursive(arr, start, end):
    if start>=end:
        return arr
    arr[start],arr[end]=arr[end],arr[start]
    return reverse_array_recursive(arr, start+1, end-1)
print(reverse_array_recursive([1,2,3,4,5], 0, 4))

def reverse_array_slicing(arr):
    return arr[::-1]
print(reverse_array_slicing([1,2,3,4,5]))