def split_array(arr):
    left_sum=0
    total_sum=sum(arr)
    count=0
    for i in range(len(arr)-1):
        left_sum+=arr[i]
        right_Sum=total_sum-left_sum
        if left_sum>right_Sum:
            count+=1
    return count
print(split_array([1,6,-3,3]))