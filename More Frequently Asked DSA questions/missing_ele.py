def missing_ele(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    sum_arr=sum(arr)
    return total-sum_arr
print(missing_ele([1,2,4,5]))