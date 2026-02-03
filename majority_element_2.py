def majority_element(nums):
    n = len(nums)
    res = []

    for i in range(n):
        count = 0
        
        # count occurrences in whole array
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        
        # check > n//3 condition
        if count > n // 3:
            # avoid duplicates before inserting
            if nums[i] not in res:
                res.append(nums[i])

        # stop early if we found 2
        if len(res) == 2:
            break

    # sort final result
    res.sort()
    return res

print(majority_element([3,2,3]))
print(majority_element([1,1,1,3,3,2,2,2]))
        