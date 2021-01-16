import unittest
import time


class MyTestCase(unittest.TestCase):
    def test_strftime(self):
        # 格式化成2016-03-20 11:45:39形式
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(dt)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
