def largest_sum_zero(arr):
    hashmap={}
    prefix_sum=0
    max_len=0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==0:
            max_len=i+1
        elif prefix_sum in hashmap:
            length=i-hashmap[prefix_sum]
            max_len=max(max_len,length)
        else:
            hashmap[i]=prefix_sum
    return max_len
print(arr[15,-2,2,15,7,-7,10,8])
            