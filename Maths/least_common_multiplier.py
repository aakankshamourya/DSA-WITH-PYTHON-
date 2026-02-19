from greatest_common_divisor import gcd
def lcm(x,y):
    return abs(x*y)//gcd(x,y)
print(lcm(18,9))