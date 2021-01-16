import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s1 = 'a'+'b'
        s2 = 'a'+'b'
        self.assertEqual(s1 is s2, True)


if __name__ == '__main__':
    unittest.main()
