import time
import unittest
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        start = time.time()
        time.sleep(0.2)
        end = time.time()
        print("总共用时%s秒" % (end - start))
        print("总共用时{}秒".format((end - start)))
        self.assertEqual(True, True)

    def test_format1(self):
        s = datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        print(s)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
