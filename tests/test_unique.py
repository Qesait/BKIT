import unittest
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random


class TestUnique(unittest.TestCase):
    def test_numbers(self):
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        result = list(Unique(data))
        answer = [1, 2]
        self.assertEqual(result, answer)

    def test_random_generator(self):
        data = gen_random(10, 1, 3)
        result = set(Unique(data))
        answer = set(range(1, 4))
        self.assertTrue(answer.issubset(result))

    def test_letters(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        result = list(Unique(data))
        answer = ['a', 'A', 'b', 'B']
        self.assertEqual(result, answer)

    def test_letters_ignoring_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        result = list(Unique(data, ignore_case=True))
        answer = ['a', 'b']
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
