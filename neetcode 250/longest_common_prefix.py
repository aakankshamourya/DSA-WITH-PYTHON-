def longest_common_prefix(strs):
    res=""
    for i in range(len(strs[0])):
        for j in strs:
            if len(j)==i or j[i]!=strs[0][i]:
                return res
        res+=strs[0][i]
print(longest_common_prefix(['flower','flow',"fly"]))