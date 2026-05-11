def commom_ele(a,b):
    res=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and a[i] not in res:
                res.append(a[i])
    return res
print(commom_ele([1,2,3,4],[3,4,5,6]))