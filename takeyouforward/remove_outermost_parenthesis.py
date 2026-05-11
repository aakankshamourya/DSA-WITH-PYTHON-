def remove_outermost_parenthesis(s):
    stack=[]
    ans=""
    for i in s:
        if i=="(":
            if stack:
                ans+=i
            stack.append(i)
        else:
            stack.pop()
            if stack:
                ans+=i
    return ans
print(remove_outermost_parenthesis("(()())(())"))