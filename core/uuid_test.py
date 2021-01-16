import unittest
import uuid

class MyTestCase(unittest.TestCase):
    def test_1(self):
        uuid1 = uuid.uuid1()
        print(str(uuid1))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
