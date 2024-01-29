import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

import copy
spam = ['A', ['B', 'C'], 'D']
cheese = copy.deepcopy(spam)
cheese[1][0] = 'X'  # Modifying a nested list in cheese should not affect spam
print(spam)
print(cheese)

import copy
original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)
shallow_copy[1][0] = 'X'
print(original_list)  # Output: [1, ['X', 3], 4]

import copy
original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)
deep_copy[1][0] = 'Y'
print(original_list)  # Output: [1, [2, 3], 4]