def gcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x%y!=0:
        rem=x%y
        x=y
        y=rem
        
    return y
print(gcd(6,3))
print(gcd(24,8))

# Recursive Solution

def gretst_c_d(x,y):
    if x==0:
        return y
    if y==0:
        return x
    return gretst_c_d(y,x%y)
print(gretst_c_d(3,2))

def grtst_common_div(x,y):
    if y!=0:
        x,y=y,x%y
    return x
print(grtst_common_div(6,2))
