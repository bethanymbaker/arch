"""
Given a set of synonyms, such as (big, large) and (eat, consume) and two sentences
Using this set, determine if two sentences with the same number of words are equivalent.

For example, given synonyms=[(big,large), (eat,consume)], the following two sentences are equivalent
He wants to eat food
He wants to consume food

Constraints:
No transitivity of synonyms, i.e. (`a`, `b`) & (`a`, `c`) do not imply (`b`, `c`)
No repeats of synonyms, e.g. `a` appears at most once in the
"""


def are_equals(s1, s2, synonyms):
    l1 = s1.split(' ')
    l2 = s2.split(' ')
    d = {}
    for tup in synonyms:
        d[tup[0]] = tup[1]
        d[tup[1]] = tup[0]

    for idx1, word1 in enumerate(l1):
        word2 = l2[idx1]
        if word1 != word2:
            if word1 in d:
                if d[word1] != word2:
                    return False
            else:
                return False
    return True


s1 = 'He wants to eat food'
s2 = 'He wants to consume food'
synonyms = [('big', 'large'), ('eat', 'consume')]
print(are_equals(s2, s1, synonyms))
