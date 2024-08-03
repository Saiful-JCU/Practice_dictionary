'''
Given two lists, one of keys and one of values, write a program to create a dictionary from these lists.
'''

def create_dictionary(keys, values):
    if len(keys) != len(values):
        raise ValueError("The number of keys and values must be same")

    dictionary = dict(zip(keys, values))
    return dictionary

keys = ['a', 'b', 'c']
values = [1,2,3]
print(create_dictionary(keys, values))

