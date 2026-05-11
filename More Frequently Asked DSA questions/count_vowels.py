def count_vowels(s):
    count=0
    vow="aeiou"
    for ch in s.lower():
        if ch in vow:
            count+=1
    return count
print(count_vowels("hello world"))  