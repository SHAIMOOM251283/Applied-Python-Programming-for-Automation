import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
print(csvWriter.writerow(['apples', 'oranges', 'grapes']))
print(csvWriter.writerow(['eggs', 'bacon', 'ham']))
print(csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam']))
csvFile.close()

#tab-separated values