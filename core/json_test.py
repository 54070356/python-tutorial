import json
import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        with open('json_test_1.json', 'r') as f:
            data = json.load(f)
            print(data)

        self.assertEqual(True, True)

    def test_2(self):
        a = {"id": "id1", "name": "名字"}
        json_str = json.dumps(a, ensure_ascii=False)
        print(json_str)
        a1 = json.loads(json_str)
        print(a1)


if __name__ == '__main__':
    unittest.main()
