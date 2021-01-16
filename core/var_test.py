a = 1


def f():
    global a
    a = 2
    print(a)


def f1():
    print(a)


if __name__ == '__main__':
    f()
    f1()
