def balance(exp):
    stack = []

    for i in exp:
        if i in '({[':
            stack.append(i)

        elif i in ')}]':
            if not stack:   # check if stack empty
                return False

            top = stack.pop()

            if i == ')' and top != '(':
                return False
            if i == ']' and top != '[':
                return False
            if i == '}' and top != '{':
                return False

        else:
            print('Invalid expression')
            return False

    return len(stack) == 0


exp = input()

if balance(exp):
    print("Balanced")
else:
    print("Not Balanced")
