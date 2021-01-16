import os
import unittest
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def test_mkdir(self):
        # create dir if not exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        self.assertEqual(True, True)



    def test_2(self):
        # 文件名和目录名
        fn = "file_test.py"
        print(os.path.dirname(fn))
        print(os.path.basename(fn))

        p = Path(fn)
        print('parent:', p.parent)
        print('name:', p.name)

        self.assertEqual(True, True)

    def test_3(self):
        """
        删除文件。如果文件不存在，会报异常
        :return:
        """
        filename = 'none_exist.bin'
        if os.path.exists(filename):
            os.remove(filename)
            print('remove ' + filename)
        else:
            print('not exist ' + filename)

        self.assertEqual(True, True)

    def test_read_text_file(self):
        for line in open("file-test.txt"):
            print(line)

        self.assertEqual(True, True)

    def test_write(self):
        """
        演示写文件
        :return:
        """
        with open('../temp/test_write.txt', 'wt') as out:
            out.write("hello1\n")
            out.write("hello2\n")

        self.assertEqual(True, True)

    def test_list_files(self):
        result = []
        path = '../demo'
        files = os.listdir(path)
        for f in files:
            if os.path.isfile(f) and f.endswith('.txt'):
                result.append(f)

        print(result)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
