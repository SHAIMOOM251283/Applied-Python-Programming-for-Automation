#import copy
#original_list = [1, [2, 3], 4]
#deep_copy = copy.deepcopy(original_list)
#deep_copy[1][0] = 'Y'
#print(original_list)  # Output: [1, [2, 3], 4]

import copy
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
# Deep copy the original grid
rotated_grid = copy.deepcopy(grid)
# Transpose the grid (swap rows with columns)
transposed_grid = list(map(list, zip(*rotated_grid)))
# Print the transposed grid as an image
for row in transposed_grid:
    print(''.join(row))




