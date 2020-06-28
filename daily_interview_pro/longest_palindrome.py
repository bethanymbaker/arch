# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.

s = "tracecars"


def is_palindrome(text):
    return text == text[::-1]


longest_palindrome = ''

for idx_1, val_1 in enumerate(s[:-1]):
    test_str = val_1
    for val_2 in s[idx_1 + 1:]:
        test_str += val_2
        if is_palindrome(test_str):
            longest_palindrome = max(longest_palindrome, test_str, key=len)

print(f'longest palindrom = {longest_palindrome}')
