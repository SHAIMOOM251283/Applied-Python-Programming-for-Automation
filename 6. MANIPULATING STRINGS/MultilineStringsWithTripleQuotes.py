spam = ('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')
print(spam)

print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

    #\n\n is used to create a blank line between "Dear Alice," and "Eve's cat has been arrested..."
    #\n\n is also used to create a blank line between the main content and the closing "Sincerely," line.
    #\n is used to create a newline after "Dear Alice," and after each sentence or line in the text.

spam = ("Dear Alice, \n\n"
        "Eve's cat has been arrested for catnapping, cat burglary, and extortion. \n\n"
        "Sincerely, \n\n"
        "Bob")
print(spam)


