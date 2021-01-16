import unittest

import requests


class MyTestCase(unittest.TestCase):
    def test_post(self):
        url = "http://localhost:18080/test"

        headers = {
            "content-type": "application/json"
        }

        data = {
            "query": {
                "text": ""
            }
        }
        resp = requests.post(url, json=data, headers=headers)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
