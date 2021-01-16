from multiprocessing import Pool


def f(x):
    return x * x


class A:
    def __init__(self):
        self.a='a'

    def f(self, x):
        return x * x

    def exec(self, data, pool):
        print(pool.map(self.f, data))


class B:
    def __init__(self):
        self.pool = Pool()


if __name__ == '__main__':
    pool = Pool()
    a = A()
    b = B()
    for i in range(1, 30):
        data = [1, 2, 3]
        a.exec(data, pool)

    print('exited')
