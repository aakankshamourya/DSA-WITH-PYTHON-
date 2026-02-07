def subarrays(arr):
    n=len(arr)
    sum=0
    for i in range(n):
        for j in range(i,n-1):
            sum+=arr[j]
            print(sum)
subarrays([1,2,3])
            