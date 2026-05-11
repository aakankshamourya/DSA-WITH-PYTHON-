def insert_sort(arr):
    for i in range(len(arr)):
        while(i>0 and arr[i]<arr[i-1]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
print(insert_sort([2,3,4,1,2,8,9]))