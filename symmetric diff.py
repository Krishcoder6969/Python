# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Calculate the symmetric difference
symmetric_diff = set1.symmetric_difference(set2)

# Print the result
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Symmetric Difference: {symmetric_diff}")
# Define two sets
set_a = {'apple', 'banana', 'orange'}
set_b = {'banana', 'grape', 'kiwi'}

# Calculate the symmetric difference using the ^ operator
symmetric_diff_operator = set_a ^ set_b

# Print the result
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Symmetric Difference (using ^ operator): {symmetric_diff_operator}")