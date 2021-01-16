import unittest


class MyTestCase(unittest.TestCase):
    def test_equals(self):
        set1 = {"a", "b"}
        set2 = {"b", "a"}
        set3 = {}
        print(set1 == set2)
        self.assertEqual(set1, set2)
        self.assertEqual(True, 'a' in set1)
        self.assertEqual(False, 'a' in set3)

    def test_update(self):
        set1 = set()
        list1 = ['a', 'b']
        set1.update(list1)
        print(set1)
        self.assertEqual(set1, {'a', 'b'})

    def test_add(self):
        s = set()
        self.assertEqual(s, set())

        s.add('a')
        self.assertEqual(s, {'a'})


if __name__ == '__main__':
    unittest.main()
