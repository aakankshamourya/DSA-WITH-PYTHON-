
def factorial(number):
    num=1
    if number==0 or number==1:
        return 1
    else:
        for i in range(1,number+1):
            num=i*num
    return num
print(factorial(4))
