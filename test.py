import unittest
from main import addNumbers 

class TestAdding(unittest.TestCase):
    def testTwoParams(self):
        self.assertEqual(addNumbers(1, 1), 2)
        self.assertEqual(addNumbers(-1, 1), 0)
        self.assertEqual(addNumbers(-0, 0), 0)

if __name__ == '__main__':
    unittest.main()
