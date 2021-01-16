import unittest
import zipfile


class MyTestCase(unittest.TestCase):
    def test_read_zip(self):
        """
        测试读取zip内的文本文件
        :return:
        """
        with zipfile.ZipFile('../test-data/zip-test.zip') as z:
            with z.open('zip-test.txt') as f:
                for line in f:
                    print(line)
                    print(line.decode())

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
