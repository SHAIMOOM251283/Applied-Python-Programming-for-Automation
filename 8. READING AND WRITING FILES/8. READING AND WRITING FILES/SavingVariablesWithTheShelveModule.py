import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

#with shelve.open('mydata') as shelf:
#    print(shelf)

#shelfFile = shelve.open('mydata')
#type(shelfFile) 
#shelfFile['cats']
#shelfFile.close()

# Open the existing shelf
shelfFile = shelve.open('mydata')
# Check the type of the shelfFile object
print(type(shelfFile))
# Retrieve and print the value associated with the key 'cats'
print(shelfFile['cats'])
#cats = shelfFile['cats']
#print(cats)
# Close the shelf file
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
