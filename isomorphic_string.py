def isomorphic(s1,s2):
    M1={}
    M2={}
    for i in range(len(s1)):
        if s1[i] not in M1:
            M1[s1[i]]=s2[i] #mapiing to both strings 
        if s2[i] not in M2:
            M2[s2[i]]=s1[i]  # mapping to both strings
        if M1[s1[i]]!=s2[i] or M2[s2[i]]!=s1[i]:
            return False
    return True
print(isomorphic("egg","add"))
print(isomorphic("foo","bar"))