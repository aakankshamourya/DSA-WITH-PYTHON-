def sum_odigits(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    return sum
print(sum_odigits(1234))