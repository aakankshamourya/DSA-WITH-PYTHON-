def permute_the_string(s1, s2):
    m = len(s1)
    n = len(s2)

    if m > n:
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26

    for i in range(m):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

    if s1_count == s2_count:
        return True

    for i in range(m, n):
        # add new character
        s2_count[ord(s2[i]) - ord('a')] += 1

        # remove old character
        s2_count[ord(s2[i - m]) - ord('a')] -= 1

        if s1_count == s2_count:
            return True

    return False


print(permute_the_string('ss', 'assbc'))  
print(permute_the_string('abc','acjdjvhk'))