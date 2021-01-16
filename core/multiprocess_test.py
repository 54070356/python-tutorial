from multiprocess import Pool


def say(s):
    print(s)


pool = Pool(1)
for d in pool.imap(say, 'hello'):
    pass

pool.close()
pool.join()
