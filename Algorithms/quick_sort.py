def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr.pop()
    greater,lesser=[],[]
    for item in arr:
        if item>pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return quick_sort(lesser)+[pivot]+quick_sort(greater)
print(quick_sort([4,9,4,1,0,5]))