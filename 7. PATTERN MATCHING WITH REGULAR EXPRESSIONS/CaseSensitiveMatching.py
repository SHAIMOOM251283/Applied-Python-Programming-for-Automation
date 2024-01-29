import re
#Ignore case
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

#Match completely different strings
#regex1 = re.compile('RoboCop')
#regex2 = re.compile('ROBOCOP')
#regex3 = re.compile('robOcop')
#regex4 = re.compile('RobocOp')