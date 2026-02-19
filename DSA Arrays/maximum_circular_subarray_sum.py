def kadanesalgo(arr):                       #maximum circular sum subarray 
    currS=arr[0]
    currmax=0
    maxtillnow=arr[0]
    for i in range(len(arr)):
        currmax=max(currmax,currS+arr[i])
        maxtillnow=max(currmax,maxtillnow)
    return maxtillnow
print(kadanesalgo([2,-3,4,3]))
print(kadanesalgo([-4,5,6,-2,3,-1,7,-10]))
print(kadanesalgo([-1,2,3,10]))
