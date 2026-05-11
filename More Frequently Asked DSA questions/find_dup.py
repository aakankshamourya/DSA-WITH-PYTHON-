def find_dup(arr):
    seen=()
    for i in range(len(arr)):
        if arr[i] in seen:
            return arr[i]
        seen+=(arr[i],)
    return None 
print(find_dup([1,2,3,4,5,2]))