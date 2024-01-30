def printTable(table):
    # Find the maximum width for each column
    col_widths = [max(map(len, col)) for col in table]

    # Transpose the table for easier processing
    transposed_table = zip(*table)

    # Print the table
    for row in transposed_table:
        # Right-justify each element based on its column width
        print(' '.join(word.rjust(width) for word, width in zip(row, col_widths)))

# Given tableData
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

# Print the table
printTable(tableData)

