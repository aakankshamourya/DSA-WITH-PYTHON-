s = "I am Aakanksha Mourya"
word = ""
ans = ""
for i in s:
    if i!=" ":
        word+=i  
    else:
        if len(word) > len(ans):
            ans = word 
            word = ""
if len(word)>len(ans):
    print(word)
else: print(ans)