import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        A = 'a'
        dict1 = {
            A: 'v'
        }

        self.assertEqual('v', dict1.get('a'))

    def test_empty(self):
        d1 = {}
        if not d1:
            print('empty')

        d2 = {'k': 'v'}
        if d2:
            print('not empty')

        else:
            print('empty')

        self.assertEqual(True, True)

    def test_case3(self):
        """
        遍历字典
        """
        self.assertEqual(True, True)

    def test_del(self):
        """
        删除元素
        """
        dict1 = {
            'a': 'av',
            'b': 'bv'
        }

        print('origin:', dict1)

        del dict1['a']
        print('del a:', dict1)

        # del dict1['c'] will raise exception
        dict1.pop('c', None)
        print('del c:', dict1)

        self.assertEqual(True, True)

    def test_size(self):
        d1 = {'k1': 'v1', 'k2': 'v2'}
        self.assertEqual(len(d1), 2)

    def test_get(self):
        d1 = {
            'k1': 'v1',
            'k2': None
        }
        self.assertEqual(d1.get('k1'), 'v1')
        self.assertEqual(d1.get('k2'), None)
        self.assertEqual(d1.get('k2', 'v2'), None)
        self.assertEqual(d1.get('k3'), None)
        self.assertEqual(d1.get('k3', 'v3'), 'v3')

    def test_set(self):
        d1 = {'k1': 'v1'}
        self.assertEqual(d1.get('k1'), 'v1')
        d1['k2'] = 'v2'
        self.assertEqual(d1.get('k2'), 'v2')

    def test_update(self):
        d1 = {'k1': 'v1', 'k2': 'v2'}
        self.assertEqual(len(d1), 2)
        d2 = {'k2': 'v2-new', 'k3': 'v3'}
        d1.update(d2)
        self.assertEqual(len(d1), 3)
        self.assertEqual(d1.get('k1'), 'v1')
        self.assertEqual(d1.get('k2'), 'v2-new')
        self.assertEqual(d1.get('k3'), 'v3')


if __name__ == '__main__':
    unittest.main()
