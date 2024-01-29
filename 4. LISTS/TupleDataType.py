eggs = ('hello', 42, 0.5)
print(eggs[0])
print( eggs[1:3])
print(len(eggs))

eggs = ('hello', 42, 0.5)
eggs[1] = 99 # Tuples cannot have their values modified, appended, or removed.
print(eggs)

print(type(('hello',))) # The comma is what lets Python know this is a tuple value.

print(type(('hello'))) # In Python, the type() function is used to determine the data type of a given object. 