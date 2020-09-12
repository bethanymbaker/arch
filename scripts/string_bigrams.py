# Write your code here.
import requests
from collections import Counter


def convert_bigram_to_index(bigram):
    hexx = ''.join(hex(ord(x))[2:] for x in bigram)
    idx = int(hexx, 16)
    return idx


def feature_vector(text):
    l = list(text)
    first_letter = l.pop(0)

    bigrams = []

    for letter in l:
        bigram = ''.join([first_letter, letter])
        bigrams.append(bigram)
        first_letter = letter

    d = {}
    for bigram in bigrams:
        if bigram in d:
            d[bigram] += 1
        else:
            d[bigram] = 1

    d_2 = {}
    assert len(d) == len(Counter(bigrams))  # Test that my code matches Counter class
    for bigram, freq in d.items():
        assert Counter(bigrams)[bigram] == freq
        idx = convert_bigram_to_index(bigram)
        d_2[idx] = freq

    l = [str(tup[0]) + ':' + str(tup[1]) for tup in sorted(d_2.items(), key=lambda x: x[0])]

    return ' '.join(l)


url = 'https://pastebin.com/raw/V5XpP3s0'
text = requests.get(url).text
print(feature_vector(text))
