def longestCommonPrefix(strs):
        #your code goes here 
        if not strs:
            return ""
        strs.sort()
        ans=[]
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return " ".join(ans)
            ans.append(first[i])
        return " ".join(ans)

print(longestCommonPrefix(["flower","flow","flight"]))