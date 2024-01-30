itemNames = []
while True:
    print('Enter the name of item ' + str(len(itemNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    itemNames = itemNames + [name] #list concatenation
print('The item names are:')
for name in itemNames:
    print(' ' + name)