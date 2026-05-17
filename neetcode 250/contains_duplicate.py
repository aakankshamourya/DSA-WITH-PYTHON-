arr = [1,2,2,3,1,1]

freq = {}

for i in arr:

    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

print(freq)
print(freq[i]>1)