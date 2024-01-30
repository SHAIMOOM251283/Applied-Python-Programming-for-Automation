spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')
#print(spam[10000]) #List index out of range.
#print(spam[1.0]) #list indices must be integers or slices, not float
print(spam[int(1.0)])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])
print(spam[0][1], spam[1][4])




