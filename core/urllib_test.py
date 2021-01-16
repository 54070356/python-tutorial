import unittest
from urllib.parse import urlparse, urlunparse


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = 'lb://service1/hello'
        r = urlparse(s)
        print(r)
        parts = ['http', '%s', r.path, r.params, r.query, r.fragment]
        s_new = urlunparse(parts)
        print(s_new)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
