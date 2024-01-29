# Binary Boolean OPerators
# The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.
binary_operator = True and True
print(binary_operator)

binary_operator = True and False
print(binary_operator)

# The or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False. 
operator = False or True
print(operator)

operator = False or False
print(operator)

# The not operator operates on only one Boolean value (or expression). The not operator simply evaluates to the opposite Boolean value.
print(not True)

print(not not not not True)

# Mixing Boolean and Comparison Operators
print((4 < 5) and (5 < 6))

print((4 < 5) and (9 < 6))

print((1 == 2) or (2 == 2))

print((2 + 2 == 4) and not (2 + 2 == 5) and (2 * 2 == 2 + 2))