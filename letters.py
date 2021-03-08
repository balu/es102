def letters(word):
    ls = set()
    for c in word:
        ls |= {c}
    return ls

def test_letters():
    assert letters("book") == {'b', 'k', 'o'}
    assert letters("few") == {'f', 'e', 'w'}

def letter_count(word):
    lc = {}
    for c in word:
        if c in lc:
            lc[c] += 1
        else:
            lc[c] = 1
    return lc

def test_letter_count():
    assert letter_count("book") == {'b': 1, 'o': 2, 'k': 1}