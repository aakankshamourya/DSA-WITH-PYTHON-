def hcf(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // hcf(a, b)
print("HCF of 12 and 15 is", hcf(12, 15))
print("LCM of 12 and 15 is", lcm(12, 15))