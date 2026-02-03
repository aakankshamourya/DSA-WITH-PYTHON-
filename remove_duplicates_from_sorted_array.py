def remove_duplicates(arr):
    n=len(arr)
    if n==0 or n==1:
        return n
    i=0
    j=i+1
    while j<n:
        if arr[i]!=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1
print(remove_duplicates([1,1,2,2,3,4,4,5]))
k=remove_duplicates([1,1,2,2,3,4,4,5])
for i in range(k):
    print(i)
    
#########################################################################################


def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return n

    i = 0
    j = i + 1

    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    return i + 1

arr = [1,1,2,2,3,4,4,5]
k = remove_duplicates(arr)

print("Non-duplicate elements:")
for i in range(k):
    print(arr[i])
