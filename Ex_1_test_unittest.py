import unittest
from Ex_1_base_for_testing import *


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("SetUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("tear Down for [" + self.shortDescription() + "]")
        print("")

    def test_something_1(self):
        self.assertEqual(check_speed(Speed(350, 3.5)),
                         "You have enought driving experience")

    def test_something_2(self):
        self.assertEqual(Speed(144, 1.7).__round__(3), 84.706)


if __name__ == '__main__':
    unittest.main()
