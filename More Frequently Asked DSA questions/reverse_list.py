def reverse_list(l):
    left=0
    right=len(l)-1
    while left<right:
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
    return l
print(reverse_list([1,2,3,4,5]))