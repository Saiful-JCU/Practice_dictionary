'''
Write a program to find the sum of all values in a dictionary.
'''

def sum_of_all_values(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum

dict = {1: 500, 2: 1500, 3:100}
print(sum_of_all_values(dict))


# alternative solution
total_sum = sum(dict.values())
print(total_sum)