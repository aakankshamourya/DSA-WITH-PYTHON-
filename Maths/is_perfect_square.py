def is_perct_sq(num):
    i=0
    while i*i<num:
        if i*i==num:
            return True
        i+=1
    return False
print(is_perct_sq(16))

def is_perfect_sq(num):
    i = 0
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False
print(is_perct_sq(49))