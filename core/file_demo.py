import os
from os.path import isfile, join
from pathlib import Path


def demo1():
    fout = open('write-demo.txt', 'wt')
    fout.write("hello1")
    fout.write("hello2")
    print('hello3', file=fout)
    fout.close()

    # override file
    f = open('write-demo.txt', 'w')
    print('hello', file=f)
    fout.close()

    # append to the end of file
    f = open('write-demo.txt', 'a')
    print('hello5', file=f)
    f.close()

    file_path = './'
    files = [join(file_path, f) for f in os.listdir(file_path) if isfile(join(file_path, f))]
    print(files)


def demo2():
    parent = Path('parent/log.txt').parent
    if parent.is_dir() and not parent.exists():
        parent.mkdir(parents=True)


if __name__ == '__main__':
    p = Path('./parent/log.txt')
    parent = p.parent
    print(parent)
    print(parent.is_dir())
    print(parent.exists())
    parent.mkdir(parents=True)
    print(parent.is_dir())
    print(parent.exists())
