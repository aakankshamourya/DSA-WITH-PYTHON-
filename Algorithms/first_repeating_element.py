def first_repeating_element(arr):
    a=[0]*(max(arr)+1)
    n=len(arr)
    for i in range(n):
        a[arr[i]]+=1
    for i in range(n):
        if a[arr[i]]>1:
            return arr[i]
    return -1
print(first_repeating_element([10,5,3,4,3,5,6]))