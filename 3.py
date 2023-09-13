import unittest

def max_number(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return -1
    try:
        return max(a, b)
    except:
        return -1

class TestMaxNumber(unittest.TestCase):

    def test_regular_values(self):
        self.assertEqual(max_number(5, 3), 5)
        self.assertEqual(max_number(2, 8), 8)
        self.assertEqual(max_number(-1, -5), -1)
        self.assertEqual(max_number(0, 0), 0)
        self.assertEqual(max_number(-3, 5), 5)

    def test_float_values(self):
        self.assertEqual(max_number(3.2, 3.1), 3.2)
        self.assertEqual(max_number(-2.5, -2.6), -2.5)

    def test_mixed_values(self):
        self.assertEqual(max_number(3, 3.1), 3.1)
        self.assertEqual(max_number(-2, -2.6), -2)

    def test_string_values(self):
        self.assertEqual(max_number("5", 3), -1)
        self.assertEqual(max_number(5, "3"), -1)
        self.assertEqual(max_number("5", "3"), -1)

    def test_none_values(self):
        self.assertEqual(max_number(None, 3), -1)
        self.assertEqual(max_number(5, None), -1)
        self.assertEqual(max_number(None, None), -1)

if __name__ == '__main__':
    unittest.main()
