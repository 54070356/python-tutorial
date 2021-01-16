import copy

dict1 = {}
dict1["a"] = 'a'
print(dict1)

# deep copy of dict
dict2 = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': {
        'k31': 'v31'
    }
}
dict2copy = copy.deepcopy(dict2)
print(dict2copy)

dict2['k3']['k31'] = 'v31-new'
print(dict2)
print(dict2copy)
