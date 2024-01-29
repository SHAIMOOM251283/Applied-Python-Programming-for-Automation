spam = 42
cheese = spam
spam = 100
cheese = spam
print(spam)
print(cheese)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)

spam = [2, 4, 6, 8, 10]
new_spam = spam
new_spam[2] = 'Hello!'
print(spam)
print(new_spam)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam.copy()  # or cheese = list(spam)
cheese[1] = 'Hello!'
print(spam)
print(cheese)