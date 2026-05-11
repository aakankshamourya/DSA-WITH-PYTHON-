def repeatedDnaSequence(str):
    seen=set()
    repeated=set()
    for i in range(len(str)-9):
        sub=str[i:i+10]
        if sub in seen:
            repeated.add(sub)
        else:
            seen.add(sub)
    return list(repeated)
print(repeatedDnaSequence("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))