import unittest
from equation_solving import get_roots


class BiquadrateTest(unittest.TestCase):
    def test_no_roots(self):
        expected_answer = set()
        self.assertEqual(expected_answer, set(get_roots(0, 0, 0)))
        self.assertEqual(expected_answer, set(get_roots(0, 1, 4)))
        self.assertEqual(expected_answer, set(get_roots(0, -1, -4)))
        self.assertEqual(expected_answer, set(get_roots(1, 0, 4)))
        self.assertEqual(expected_answer, set(get_roots(-1, 0, -4)))

    def test_one_root(self):
        expected_answer = {0}
        self.assertEqual(expected_answer, set(get_roots(0, 1, 0)))
        self.assertEqual(expected_answer, set(get_roots(1, 0, 0)))
        self.assertEqual(expected_answer, set(get_roots(0, -1, 0)))
        self.assertEqual(expected_answer, set(get_roots(-1, 0, 0)))

    def test_two_roots(self):
        expected_answer = {-2, 2}
        self.assertEqual(expected_answer, set(get_roots(0, 1, -4)))
        self.assertEqual(expected_answer, set(get_roots(0, -1, 4)))
        self.assertEqual(expected_answer, set(get_roots(1, 0, -16)))
        self.assertEqual(expected_answer, set(get_roots(-1, 0, 16)))

    def test_three_roots(self):
        expected_answer = {-2, 0, 2}
        self.assertEqual(expected_answer, set(get_roots(1, -4, 0)))
        self.assertEqual(expected_answer, set(get_roots(-1, 4, 0)))

    def test_four_roots(self):
        expected_answer = {-3, -1, 1, 3}
        self.assertEqual(expected_answer, set(get_roots(1, -10, 9)))
        self.assertEqual(expected_answer, set(get_roots(-1, 10, -9)))


if __name__ == '__main__':
    unittest.main()
