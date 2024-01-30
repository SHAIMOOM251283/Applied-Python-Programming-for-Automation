import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())


#greedyHaRegex = re.compile(r'(Ha){3,5}')
#Varying number of consecutive 'Ha' sequences
#input_strings = [
#    'HaHaHa',          # Match: HaHaHa
#    'HaHaHaHa',        # Match: HaHaHaHa
#    'HaHaHaHaHa',      # Match: HaHaHaHaHa
#    'HaHaHaHaHaHa',    # Match: HaHaHaHaHa
#    'HaHaHaHaHaHaHa',  # Match: HaHaHaHaHa
#]
#for string in input_strings:
#    mo = greedyHaRegex.search(string)
#    if mo:
#        print(f"Matched '{mo.group()}' in '{string}'")
#    else:
#        print(f"No match in '{string}'")
