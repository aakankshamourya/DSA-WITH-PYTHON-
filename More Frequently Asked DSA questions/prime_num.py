def prime_number(num):
    if num<2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print(prime_number(9))
print(prime_number(11))
    