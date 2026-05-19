def merge_two_sorted_array(arr1,arr2,m,n):
    while m>0 and n>0:
        if arr1[m-1]>arr2[n-1]:
            arr1[m+n-1] = arr1[m-1]
            m-=1
        else:
            arr1[m+n-1] = arr2[n-1]
            n-=1
    return arr1
print(merge_two_sorted_array([1,2,3,0,0,0], [2,5,6], 3, 3))