import re
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(' ' in 'hello word')
        print(' ' in 'helloword')
        self.assertEqual(True, True)

    def test_split1(self):
        s = 'a/b.py'
        sp = s.split('/')
        print(sp[-1])
        s_path = '/'.join(sp[0:-1])
        print(s_path)
        print('.'.join(sp))
        self.assertEqual(s_path, 'a')

    def test_split2(self):
        s = 'b.py'
        sp = s.split('/')
        if len(sp) > 1:
            self.assertEqual(True, False)

    def test_split3(self):
        s = 'a='
        sp = s.split('=')
        print(sp)
        self.assertEqual(len(sp), 1)

    def test_join(self):
        s = 'ab'
        sp = '。'.join(s)
        print(sp)

        s = ['ab', 'c']
        sp = '。'.join(s)
        print(sp)
        self.assertEqual(True, True)

    def test_replace(self):
        s = '  \na b a\na    c '
        print('start')
        s1 = s.strip()
        print('s1:%s' % s1)
        re_blank1 = re.compile(r'\s+')
        s2 = re_blank1.sub(' ', s)
        print('s2:%s' % s2)
        re_blank2 = re.compile(r'\s{2,}')
        s3 = re_blank2.sub(' ', s2)
        print('s3:%s' % s3)

        # print(s.split('(\\s+)'))
        self.assertEqual(True, True)

    def test_find(self):
        s = ' ab -- c -- d '
        pos = s.find(' -- ')
        print(s[pos + 4:])

        self.assertEqual(True, True)

    def test_too_long(self):
        s = 'More than 91.6 million Americans have voted so far, as a majority of states are reporting record early ' \
            'More than 91.6 million Americans have voted so far, as a majority of states are reporting record early '
        print('More than 91.6 million Americans have voted so far, as a majority of states are reporting record early '
              'voting turnout in the 2020 election. While  too soon to know how that record turnout will translate to '
              'Election Day, the massive early voting numbers suggest a high level of enthusiasm for voting this '
              'year, despite the obstacles of a pandemic.')
        self.assertEqual(True, True)

    def test_strip(self):
        s = '你好 \n \t'
        self.assertEqual(s.strip(), '你好')


if __name__ == '__main__':
    unittest.main()
