def gcd(num1,num2):
    while num2:
        num1,num2=num2,num1%num2
    return num1
print(gcd(18,9))


def lcm(x,y):
    return abs(x*y)//gcd(x,y)
print(lcm(18,9))