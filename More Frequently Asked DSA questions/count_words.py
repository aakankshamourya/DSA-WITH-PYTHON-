def count_words(s):
    count=0
    for ch in s:
        if ch==" ":
            count+=1
    return count+1
print(count_words("hello world"))