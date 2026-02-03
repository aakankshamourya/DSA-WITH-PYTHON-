def subarray_sum(arr):
    n=len(arr)
    max_sum=float('-inf')
    current_sum=0
    for i in range(n):
        current_sum+=arr[i]
        if current_sum>max_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
    return max_sum                              
print(subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
print(subarray_sum([1,2,3,4,5]))


def subarray_sum(arr):
    n=len(arr)
    result=0
    for i in range(n):
        result+=arr[i]*(i+1)*(n-i)
    return result
print(subarray_sum([1,2,3]))