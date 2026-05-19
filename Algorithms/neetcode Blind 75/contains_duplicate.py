def Duplicate(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
print(Duplicate([1,1,2,3]))
print(Duplicate([1,2,3,4]))
    
        
    