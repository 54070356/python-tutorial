import json
from collections import namedtuple

Address = namedtuple('Address', ['city', 'street'])

User = namedtuple('User', ['id', 'name', 'age', 'address'])

if __name__ == '__main__':
    address = Address('beijing', 'street1')

    user = User('id-1', 'Tome', 10, address)

    print(user)
    print(json.dumps(user))

    print('id='+user['id'])
