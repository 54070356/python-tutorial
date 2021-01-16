import time
import unittest


class MyTestCase(unittest.TestCase):
    def test_for_1(self):
        for i in range(10):
            print(i)
            try:
                if i < 6:
                    raise Exception('break')
                else:
                    break
            except:
                print('sleep')
                time.sleep(1)


        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
