def maxSubArraySum(arr):
    currsum=0
    maxsum=arr[0]
    for n in arr:
        if currsum<0:
            currsum=0
        currsum+=n
        maxsum=max(maxsum,currsum)
    return maxsum
print(maxSubArraySum([-1,2,9,2,3,-3]))
        
    