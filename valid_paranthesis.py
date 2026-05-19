def isValid(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    
    for ch in s:
        if ch in mapping.values():   # opening
            stack.append(ch)
        else:                        # closing
            if not stack or stack.pop() != mapping[ch]:
                return False
    
    return not stack
print(isValid("(((}}}{{{()}}})))"))
print(isValid("()[]{}"))
print(isValid("(]"))