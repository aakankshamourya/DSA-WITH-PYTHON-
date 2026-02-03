def longest_word(s):
        res=0
        longest_len=0
        n=len(s)
        for i in range(n):
            if s[i]!=" ":
                longest_len+=1
            else:
                res=max(res,longest_len)
                longest_len=0
        return res
print(longest_word("I am Aakanksha Mourya"))