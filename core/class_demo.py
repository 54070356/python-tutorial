import json


class A:
    def __init__(self):
        self.prop1 = "A prop1"

    def to_dict(self):
        return self.__dict__


class B(A):
    def __init__(self):
        self.prop1 = "B prop1"
        self.prop2 = "B prop2"
        self.prop3 = {"nest":"nest1"}


a = A()
a.prop2 = 'prop2'
print(a.prop2)
a.prop3 = 'prop3'
print(a.prop3)
b = B()
print(b.to_dict())
print(json.dumps(b.to_dict()))
