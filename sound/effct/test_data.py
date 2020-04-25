import unittest

class Testone(unittest.TestCase):

    def setUp(self):
        print("---setup---")

    def tearDown(self):
        print("---testdown---")

    def test_2(self):
        a=1
        b=1
        self.assertEqual(a,b)