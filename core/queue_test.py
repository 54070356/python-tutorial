import logging
import unittest
from queue import Queue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #logging.basicConfig(level=logging.INFO)
        queue = Queue(maxsize=2)
        try:
            queue.put('a', False)
            queue.put('b', False)
            queue.put('c', False)
        except Exception as e:
            logging.error("error occurs", exc_info=True)

        self.assertEqual(True, True)

    def test_get(self):
        queue = Queue(maxsize=2)
        try:
            queue.get(True, 5)
        except Exception as e:
            logging.error("error occurs", exc_info=True)

        self.assertEqual(True, True)
if __name__ == '__main__':
    unittest.main()
