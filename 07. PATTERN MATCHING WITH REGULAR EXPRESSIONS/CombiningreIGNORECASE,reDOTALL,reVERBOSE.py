import re

#someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
#result_search = someRegexValue.search('Foo\nbar\nBaz')
#print(result_search.group())
#print((result_search := someRegexValue.search('Foo\nbar\nBaz')).group())
#result_findall = someRegexValue.findall('foo Foo FOO Foo\nbar\nBaz')
#print(result_findall)
#print(result_findall := someRegexValue.findall('foo Foo FOO Foo\nbar\nBaz'))

#someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
#print((result_search := someRegexValue.search('Foo\nbar\nBaz')).group())
#print(result_findall := someRegexValue.findall('foo Foo FOO Foo\nbar\nBaz'))


# Without re.VERBOSE
pattern_without_verbose = re.compile(r'\d{4}-\d{2}-\d{2}')

# With re.VERBOSE
pattern_with_verbose = re.compile(r'''
    \d{4}  # Year
    -      # Separator
    \d{2}  # Month
    -      # Separator
    \d{2}  # Day
''', re.VERBOSE)

# Test strings
test_string = 'Date: 2022-01-01'

# Without re.VERBOSE
result_without_verbose = pattern_without_verbose.search(test_string)
print("Without re.VERBOSE:", result_without_verbose.group())

# With re.VERBOSE
result_with_verbose = pattern_with_verbose.search(test_string)
print("With re.VERBOSE:", result_with_verbose.group())
