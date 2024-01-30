import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
print(outputWriter.writerow([1, 2, 3.141592, 4]))
outputFile.close()

#The numbers printed in the terminal are the return values of the writerow method calls. 
#The writerow method writes a row to the CSV file and returns the number of characters written.
#In your code:
    #print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])) writes the row ['spam', 'eggs', 'bacon', 'ham'] to the CSV file and returns the number of characters written, which is 21.
    #print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])) writes the row ['Hello, world!', 'eggs', 'bacon', 'ham'] to the CSV file and returns the number of characters written, which is 32.
    #print(outputWriter.writerow([1, 2, 3.141592, 4])) writes the row [1, 2, 3.141592, 4] to the CSV file and returns the number of characters written, which is 16.
#So, the numbers 21, 32, and 16 represent the number of characters written to the file for each corresponding writerow call.