def revese_words_in_string(string):
    words=string.split()
    words.reverse()
    return " ".join(words)
print(revese_words_in_string("Hello World"))

def revese_words_in_string_builtin(string):
    return " ".join(reversed(string.split()))
print(revese_words_in_string_builtin("Hello World"))

def revese_words_in_string_slicing(string):
    return " ".join(string.split()[::-1])
print(revese_words_in_string_slicing("Hello World"))

def revese_words_in_string_loop(string):
    words=string.split()
    reversed_string=""
    for word in reversed(words):
        reversed_string+=word+" "
    return reversed_string.strip()
print(revese_words_in_string_loop("Hello World"))

def revese_words_in_string_recursion(string):
    words=string.split()
    if len(words)==1:
        return words[0]
    else:
        return revese_words_in_string_recursion(" ".join(words[1:]))+" "+words[0]
print(revese_words_in_string_recursion("Hello World"))

def revese_words_in_string_stack(string):
    words=string.split()
    stack=[]
    for word in words:
        stack.append(word)
    reversed_string=""
    while stack:
        reversed_string+=stack.pop()+" "
    return reversed_string.strip()