def pal(n):
    original_num=n
    rev=0
    while original_num>0:
        remainder=original_num%10
        rev=rev*10+remainder
        original_num=original_num//10
    if rev==n:
        return True
    else:
        return False
print(pal(121))
print(pal(345))
    