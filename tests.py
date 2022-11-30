import unittest
from types import GeneratorType
from itertools import islice
from lucky_numbers import lucky_numbers


class TestLuckyNumbers(unittest.TestCase):
    def test_is_generator(self):
        self.assertIsInstance(lucky_numbers(), GeneratorType)

    def test_values(self):
        result = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33,
                  37, 43, 49, 51, 63, 67, 69, 73, 75, 79,
                  87, 93, 99, 105, 111, 115, 127, 129, 133,
                  135, 141, 151, 159, 163, 169, 171, 189, 193,
                  195, 201, 205, 211, 219, 223, 231, 235, 237,
                  241, 259, 261, 267, 273, 283, 285, 289, 297,
                  303, 307, 319, 321, 327, 331, 339, 349, 357,
                  361, 367, 385, 391, 393, 399, 409, 415, 421,
                  427, 429, 433, 451, 463, 475, 477, 483, 487,
                  489, 495, 511, 517, 519, 529, 535, 537, 541,
                  553, 559, 577, 579, 583, 591, 601, 613, 615,
                  619, 621, 631, 639, 643, 645, 651, 655, 673,
                  679, 685, 693, 699, 717, 723, 727, 729, 735,
                  739, 741, 745, 769, 777]
        answer = list(islice(lucky_numbers(), len(result)))
        self.assertEqual(result, answer)

    def test_first_ten(self):
        result = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
        numbers = lucky_numbers()
        for i in range(10):
            self.assertEqual(result[i], numbers.__next__())


if __name__ == '__main__':
    unittest.main()