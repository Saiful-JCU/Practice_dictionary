'''
Write a program to merge two dictionaries into one.
'''

def merge_dictionaries(dict1, dict2):
    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    return merge_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}

print(merge_dictionaries(dict1, dict2))
