import unittest
from simple import avrg


class TestMyCode(unittest.TestCase):
    
    def test_numbers(self):
        result = avrg(1,3,5,67,78,2,33,6,7,23)
        self.assertEqual(result,22.5)

if __name__ == '__main__':
    unittest.main()

