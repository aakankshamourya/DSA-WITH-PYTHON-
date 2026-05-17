def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==target:
                return arr[i],arr[j]
print(two_sum([1,2,3,4,5,6,7,8,9],9))

def two_sum(array,target):
    res=0
    for i in range(len(array)):
        second=target-array[i]
        if second in array:
            return second,array[i]
print(two_sum([6,7,8,9,0,5,3],14))