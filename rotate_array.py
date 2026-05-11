def rotate_Array(arr,k):
    n=len(arr)
    def reverse(left,right):
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    return arr
print(rotate_Array([1,2,3,4,5,6,7,8,9],3))
    
    
    