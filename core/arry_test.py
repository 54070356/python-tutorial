import unittest


class MyTestCase(unittest.TestCase):
    def test_slice(self):
        """
        a[start:stop]  # items start through stop-1
        a[start:]      # items start through the rest of the array
        a[:stop]       # items from the beginning through stop-1
        a[:]           # a copy of the whole array
        a[start:stop:step] # start through not past stop, by step
        :return:
        """

        a = [0, 1, 2, 3, 4]

        self.assertEqual(a[:2], [0, 1])

        self.assertEqual(a[:5], [0, 1, 2, 3, 4])

        self.assertEqual(a[-1], 4)
        self.assertEqual(a[-2], 3)
        self.assertEqual(a[:-2], [0, 1, 2])

        self.assertEqual(a[:-1:-1], [])
        self.assertEqual(a[2:-1:-1], [])

        self.assertEqual(a[0:-1:-1], [])

        self.assertEqual(a[:1:1], [0])

        # all items in the array, reversed
        self.assertEqual(a[::-1], [4, 3, 2, 1, 0])

        # the first two items, reversed
        self.assertEqual(a[1::-1], [1, 0])

        # everything except the last two items, reversed
        self.assertEqual(a[-3::-1], [2, 1, 0])

        self.assertEqual(a[2:1:-1], [2])

        self.assertEqual(a[-2:-3:-1], [3])

        self.assertEqual(a[:-3:-1], [4, 3])

    def test_empty(self):
        a = None
        if a:
            self.fail()

        a = []
        if a:
            self.fail()



if __name__ == '__main__':
    unittest.main()
