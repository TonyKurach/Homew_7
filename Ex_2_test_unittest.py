import unittest
from Ex_2_base_for_testing import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.book = Book("Товарищ жандарм", "Станислав Сергеев", "АСТ", 2015, 205, 27.42, "Мягкий переплет")

    def test_price(self):
        self.assertEqual(self.book.get_price(), 27.42)

    def test_num_pages(self):
        self.assertGreater(self.book.get_num_pages(), 150)

    def test_year_publish(self):
        self.assertLess(self.book.get_year(), 2017)

if __name__ == '__main__':
    unittest.main()
