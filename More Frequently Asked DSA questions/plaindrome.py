def palid(num):
    original=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev==original
print(palid(121))
print(palid(123))