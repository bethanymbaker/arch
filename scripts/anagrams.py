import re


def is_match(str1, str2, schars=[]):
    if len(schars) > 0:
        pattern = f"[{''.join(schars)}]"
        str1 = re.sub(pattern, '', str1)
        str2 = re.sub(pattern, '', str2)
    if len(str1) != len(str2):
        return False
    l1 = sorted(list(str1))
    l2 = sorted(list(str2))
    return ''.join(l1) == ''.join(l2)


str1 = 'eat'
str2 = 'ate'
print(is_match(str1, str2))

str1 = 'good'
str2 = '*doog!'
print(is_match(str1, str2, schars=['*', '!']))
