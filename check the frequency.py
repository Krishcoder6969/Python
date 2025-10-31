test_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
value_frequencies = {}

for value in test_dict.values():
    if value in value_frequencies:
        value_frequencies[value] += 1
    else:
        value_frequencies[value] = 1

print(f"The original dictionary: {test_dict}")
print(f"The frequency of values: {value_frequencies}")
from collections import Counter

test_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

value_frequencies = Counter(test_dict.values())

print(f"The original dictionary: {test_dict}")
print(f"The frequency of values: {value_frequencies}")
test_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
values_list = list(test_dict.values())
unique_values = list(set(values_list))
value_frequencies = {}

for value in unique_values:
    value_frequencies[value] = values_list.count(value)

print(f"The original dictionary: {test_dict}")
print(f"The frequency of values: {value_frequencies}")