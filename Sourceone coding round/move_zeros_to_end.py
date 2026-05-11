def move_eros_to_end(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
print(move_eros_to_end([1,2,0,0,0,1,1,2,3]))