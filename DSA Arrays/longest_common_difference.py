def common_diff_longest_subarray(arr):
     n=len(arr)
     dif=arr[1]-arr[0]
     max_len=2
     curr_len=2

     for i in range(2,n):
         diff=arr[i]-arr[i-1]                   
         if diff==dif:
            curr_len+=1
         else:
           curr_len=2
         max_len=max(max_len,curr_len)
     return max_len
print(common_diff_longest_subarray([2,4,6,8,9,10]))
print(common_diff_longest_subarray([1,2,3,4,5,6]))