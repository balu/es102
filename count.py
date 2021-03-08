def letter_count(word):
    cs = {}
    for letter in word:
        if letter in cs.keys():
            cs[letter] += 1
        else:
            cs[letter] = 1
    return cs

print(letter_count("Bookkeeper"))