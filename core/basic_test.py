import unittest


class MyTestCase(unittest.TestCase):
    def test_return(self):
        def f1():
            a = 'a'
            b = 'b'
            return a, b

        r1, _ = f1()
        self.assertEqual(r1, 'a')
        r1, *_ = f1()
        self.assertEqual(r1, 'a')

        r1, r2 = f1()
        self.assertEqual(r2, 'b')




if __name__ == '__main__':
    unittest.main()
