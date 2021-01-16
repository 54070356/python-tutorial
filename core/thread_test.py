import threading
import time
import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        t = threading.Thread(target=self.long_time_task, args=())
        t.setDaemon(True)
        t.start()
        t.join(4)
        self.assertEqual(True, True)

    def long_time_task(self):
        print('long time task starts')
        time.sleep(2)
        print('long time task ends')

    def test_timer(self):
        def hello():
            print('hello')

        def sorry():
            raise Exception('sorry')

        timer1 = threading.Timer(0.2, sorry)
        timer1.start()

        timer2 = threading.Timer(1, hello)
        timer2.start()
        print('end')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
