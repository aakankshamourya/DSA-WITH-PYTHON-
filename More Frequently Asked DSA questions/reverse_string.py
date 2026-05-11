def reverse_string(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    return res
print(reverse_string("hello"))
    
    
def reverse_Str(s):
    rev_string=''
    for i in range(len(s)-1,-1,-1):
        rev_string+=s[i]
    return  rev_string
print(reverse_Str('akanksha'))

def reverse_sen(s):
    s=s.split()
    result=[]
    for i in range(len(s)-1,-1,-1):
        result.append(s[i])
    return ' '.join(result)
print(reverse_sen('akanksha Mourya'))
    