import unittest

class Testone(unittest.TestCase):

    def setUp(self):
        print("---setup1---")

    def tearDown(self):
        print("---testdown1---")

    def test_1(self):
        a=1
        b=1
        self.assertEqual(a,b)