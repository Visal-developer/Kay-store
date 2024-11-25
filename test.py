
my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sort by keys
sorted_keys = sorted(my_dict.keys())
print(sorted_keys)  # Output: ['a', 'b', 'c']

# Sort by values
sorted_by_values = sorted(my_dict.items(), key=lambda item: item[2])
print(sorted_by_values)  # Output: [('a', 1), ('c', 2), ('b', 3)]


