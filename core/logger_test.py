import logging
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(__name__)
        logger = logging.getLogger(__name__)
        print(logger)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
