import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = os.path.join('demo1/os_path_test.py', '.*path.*.json')
        print(s)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
