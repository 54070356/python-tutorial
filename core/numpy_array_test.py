import unittest

import numpy as np


class MyTestCase(unittest.TestCase):
    def test_slice(self):
        a = np.array([0, 1, 2, 3, 4])
        print(a[:-3:-1])

        print(a[:-2:-1])
        self.assertEqual([4], a[:-2:-1])

    def test_argsort(self):
        a = np.array([0.4, 0.2, 0.3])
        print(a.argsort())

        self.assertEqual(True, (np.array([0, 1, 2]) == a.argsort()).all())


if __name__ == '__main__':
    unittest.main()
