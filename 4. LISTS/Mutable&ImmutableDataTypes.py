name = 'Zophie a cat'
#name[7] = 'the' #A string is immutable. It cannot be changed.
#print(name)

#name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12] # The proper way to “mutate” a string is to use slicing and concatenation to build a new string.
print(name)
print(newName)

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

eggs = [1, 2, 3]
eggs.extend([4, 5, 6])
print(eggs)

eggs = [1, 2, 3]
eggs.extend((4, 5, 6))  # Using a tuple
print(eggs)

eggs = [1, 2, 3]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

eggs = [1, 2, 3]
eggs[0:3] = [4, 5, 6]
print(eggs)

eggs = [1, 2, 3]
eggs.clear()
eggs.extend([4, 5, 6])
print(eggs)
