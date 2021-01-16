import shutil
import unittest
import pathlib


class MyTestCase(unittest.TestCase):
    def test_delete_dir(self):
        a_dir = 'logs'
        shutil.rmtree(a_dir)
        self.assertEqual(True, True)

    def test_parent(self):
        fn = 'dir_test.py'
        print(pathlib.Path(fn).parent)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
