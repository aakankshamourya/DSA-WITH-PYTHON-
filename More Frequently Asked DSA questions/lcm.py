def lcm(x, y):
    greater=max(x, y)
    while True:
        if greater%x==0 and greater%y==0:
            return greater
        greater+=1
print(lcm(18,9))