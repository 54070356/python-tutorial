import unittest
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def test_something(self):
        parent = Path(".").absolute().parent
        print("path={}".format(parent))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
