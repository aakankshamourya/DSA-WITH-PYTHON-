def repeatinng_ele(arr):
    seen={}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]!=arr[j]:
                continue
            else:
                return arr[i]
print(repeatinng_ele([1,2,3,4,5,3,2,1]))
                