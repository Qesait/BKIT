import unittest
from lab_python_fp.field import field


class TestField(unittest.TestCase):
    def setUp(self):
        self.goods = [
           {'title': 'Ковер', 'price': 2000, 'color': 'green'},
           {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]

    def test_one_argument(self):
        result = list(field(self.goods, 'title'))
        answer = ['Ковер', 'Диван для отдыха']
        self.assertEqual(result, answer)

    def test_many_arguments(self):
        result = list(field(self.goods, 'title', 'price'))
        answer = [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
