def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(sort([64,34,25,12,22,11,90]))



def bubble_sort(arr):
    has_swapped=True
    num_iteration=0
    
    while has_swapped:
        has_swapped=False
        for i in range(len(arr)-num_iteration-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                has_swapped=True
        num_iteration+=1
    return arr
print(bubble_sort([9,1,28,3]))

def bubble_sort_optimized(arr):
    has_swapped=True
    num_iteration=0
    
    while has_swapped:
        has_swapped=False
        for i in range(len(arr)-num_iteration-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                has_swapped=True
        num_iteration+=1
    return arr
print(bubble_sort_optimized([9,1,28,3]))