spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
#spam.sort()
spam.sort(reverse=True)
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
sorted_spam_ascending = sorted(spam)
sorted_spam_descending = sorted(spam, reverse=True)
print("Ascending Sort:", sorted_spam_ascending)
print("Descending Sort:", sorted_spam_descending)

#spam = [1, 3, 2, 4, 'Alice', 'Bob']
#spam.sort() #TypeError: '<' not supported between instances of 'str' and 'int'
#print(spam)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
#spam.sort(key=str.lower)
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)