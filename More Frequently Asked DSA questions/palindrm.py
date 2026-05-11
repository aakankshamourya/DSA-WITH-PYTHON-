def pal(num):
    original=num
    rev=0
    for i in range(len(str(num))):
        rem=num%10
        rev=rev*10+rem
        num=num//10
        
    return original==rev
print(pal(121))
        
    