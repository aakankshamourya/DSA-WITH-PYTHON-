def rcrd_brkng_day(arr):
    rbd=0
    n=len(arr)
    for i in range(n):
        if n==1:
            rbd=1
        elif i==0 and arr[i]>arr[i+1]:
            rbd+=1  
        elif i==n-1 and arr[i]>arr[i-1]:
            rbd+=1
        elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            rbd+=1
    return rbd
print(rcrd_brkng_day([10,20,30,40,50]))
            
    