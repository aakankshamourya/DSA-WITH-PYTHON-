def magicNumber(n):
    result = 0
    x = 1
    j = 1
    while n:
        k = n & x
        result += k * (5**j)
        j += 1
        n = n>>1
    print(result)

print(magicNumber(6))