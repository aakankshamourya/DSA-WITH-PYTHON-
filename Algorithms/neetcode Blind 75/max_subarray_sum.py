def maxSubArraySum(arr):
    currsum=0
    maxsum=arr[0]
    for i in range(len(arr)):
        if currsum<0:
            currsum=0
        currsum+=arr[i]
        maxsum=max(maxsum,currsum)
    return maxsum
print(maxSubArraySum([-1,2,9,2,3,-3]))
        
    