def reverse_words_od_string(str):
    str=str.split()
    str.reverse()
    return " ".join(str)
print(reverse_words_od_string("Hello World"))


