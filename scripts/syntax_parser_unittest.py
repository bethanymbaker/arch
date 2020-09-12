# Write your code here.
import unittest


def code_is_valid(text):
    d = {'{': 1, '}': -1, '[': 2, ']': -2, '(': 3, ')': -3}
    l = [d[val] for val in list(text) if val in d]

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

    return len(queue) == 0


class ExampleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(code_is_valid('{[a + b](c*d)}'), True)
        self.assertEqual(code_is_valid('foo[{]'), False)
        self.assertEqual(code_is_valid('{[(])}'), False)
        self.assertEqual(code_is_valid('{}'), True)
        self.assertEqual(code_is_valid('['), False)
        self.assertEqual(code_is_valid('{({[]})}'), True)


if __name__ == '__main__':
    unittest.main()
