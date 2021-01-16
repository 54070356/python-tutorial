def f1(*args, msg):
    for arg in args:
        print('arg=',arg)

    print('msg=',msg)


f1('a', 'b', msg="hello")
f1('a', 'b', "hello")