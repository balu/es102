s = "Why, sometimes I’ve believed as many as six impossible things before breakfast."

def wordlist(sentence):
    words = sentence.split(" ")
    clean = []
    for word in words:
        clean.append(word.rstrip(",.").lower())
    return sorted(clean)

print(wordlist(s))
