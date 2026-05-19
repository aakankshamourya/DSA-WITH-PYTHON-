def print_all_subarrays(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(arr[k],end=" ")
            print()
print_all_subarrays([1,2,3])



################################################################################################


def all_subarrays(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(arr[k],end=" ")
            print()
all_subarrays([4,5,6])
            
            
    