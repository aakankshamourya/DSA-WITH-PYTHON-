def arrays(arr,start,end,val):
    while start<end:
        mid=(start+end)//2
        if val==arr[mid]:
            return mid
        elif val>=arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
print(arrays([2,3,4,5,6],0,4,2))
    