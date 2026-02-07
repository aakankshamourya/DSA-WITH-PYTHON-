def reverseSen(s):
    stack=[]
    temp=""
    for i in s:
        if i==" ":
            stack.append(temp)
            temp=""
        else:
            temp=temp+i
    stack.append(temp)
    while len(stack)>0:
        print(stack.pop(),end=" ")
print(reverseSen("Aakanksha Mourya"))