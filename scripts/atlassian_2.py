def is_balanced(str):
    d = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
    l = [d[val] for val in list(str) if val in d]
    queue = []
    for val in l:
        if val > 0:
            queue.append(val)
        else:
            if len(queue) < 1:
                return False
            old_val = queue.pop()
            if val + old_val != 0:
                return False
    return not len(queue) > 0


str = "(a+b)"  # True
str = ")a+b("  # False
str = "(a+b))"  # False
str = "[(a+b)]"  # True
str = "[(a+b)+{c+d}]"  # True
str = "[(a+b)+}c+d{]"  # False
str = "((("
str = ")))"
print(is_balanced(str))
