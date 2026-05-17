def sort_array(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
                
    return arr
print(sort_array([4,3,4,2,4,1,1,3]))