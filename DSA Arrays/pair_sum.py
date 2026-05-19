def pair_sum(arr,target):
    pairs=[]
    seen=set()
    for num in arr:
        complement=target-num
        if complement in seen:
            pairs.append((complement,num))
            seen.add(num)
        else:
            seen.add(num)
    return pairs
print(pair_sum([1,2,3,4,5,6],7))
print(pair_sum([10,15,3,7,5,8],17))

#####################################################################################################

def pair_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return (arr[i],arr[j])
print(pair_sum([1,2,3,4,5,6],7))
print(pair_sum([10,15,3,7,5,8],17))


#####################################################################################################
def pair_sum(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return (arr[left],arr[right])
        elif current_sum<target:
            left+=1
        else:
            right-=1    
    return None
print(pair_sum([1,2,3,4,5,6],7))