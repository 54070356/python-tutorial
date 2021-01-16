import unittest
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str = 'tom'
    age: int = 12


class MyTestCase(unittest.TestCase):
    def test_something(self):
        person = Person('Jack', 10)
        print(person)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
