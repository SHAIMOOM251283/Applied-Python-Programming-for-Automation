catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'
print(catName1)
print(catName2)
print(catName3)
print(catName4)
print(catName5)
print(catName6)

# A DIFFERENT METHOD OF THE ABOVE
cat_names = ['Zophie', 'Pooka', 'Simon', 'Lady Macbeth', 'Fat-tail', 'Miss Cleo']
for cat_name in cat_names:
    print(cat_name)

print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()

print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

print(f'The cat names are: {catName1} {catName2} {catName3} {catName4} {catName5} {catName6}') #f-string
print('The cat names are: {} {} {} {} {} {}'.format(catName1, catName2, catName3, catName4, catName5, catName6)) #format method
