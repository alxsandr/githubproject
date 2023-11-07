import unittest
from simple import avrg


class TestMyCode(unittest.TestCase):

    def test_negative(self):
        result = avrg(-1,-8,-12,-50)
        self.assertEqual(result,-17.75)

if __name__ == '__main__':
    unittest.main()

