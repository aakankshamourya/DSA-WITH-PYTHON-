
#aer permutation boty strings should be same
def anagram(str1,str2):
    return sorted(str1)==sorted(str2)
print(anagram("listen","silent"))