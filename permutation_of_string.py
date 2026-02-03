def heap_perm(s):
    s = list(s)
    res = []

    def generate(n):
        if n == 1:
            res.append("".join(s))
            return
        for i in range(n):
            generate(n-1)
            if n % 2 == 1:
                s[0], s[n-1] = s[n-1], s[0]
            else:
                s[i], s[n-1] = s[n-1], s[i]

    generate(len(s))
    return res

print(heap_perm("abc"))
print(heap_perm("asdhj"))