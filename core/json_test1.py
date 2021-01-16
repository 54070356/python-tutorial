import json


class A:
    def __init__(self):
        self.prop1 = "value1"
        self.prop_2 = "value_2"
        self.prop3 = {"a":"a1", "b":1}

    def get_prop1(self):
        return self.prop1

    def get_prop_2(self):
        return self.prop_2


if __name__ == '__main__':
    a = A()
    s = json.dumps(a.__dict__)
    print(s)