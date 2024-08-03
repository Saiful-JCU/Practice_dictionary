'''
we can print all the values in the dictionary using values() method.
'''

info = { 'name': 'saiful', 'age': 22, 'eligibility': True}
print(info.values())

for key in info.keys():
    print(f'the value corresponding to the key "{key}" is {info[key]}  ')

