def palind(str):
    l=0
    r=len(str)-1
    while l<r:
        if str[l]!=str[r]:
            return False
        l+=1
        r-=1
        return True
print(palind("saaa"))
print(palind("aakaa"))