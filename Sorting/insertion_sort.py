def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i],arr[i-1]=arr[i-1],arr[i]
            
            i-=1
    return arr
print(insertion_sort([1,5,3,7,8,3,4]))
    