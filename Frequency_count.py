'''
Write a program to count the frequency of each character in a given string and store the result in a dictionary.
'''

def count_character_frequency(str):
    frequency_dict = {}

    for char in str:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict
str = input("write your sentence: ")
print(count_character_frequency(str))
