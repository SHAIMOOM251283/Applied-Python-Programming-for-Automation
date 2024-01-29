import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
#print(mo2 == None)
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
#print(mo3.group()) #Attribute Error

#batRegex = re.compile(r'Bat(wo)*man')
#mo1 = batRegex.search('The Adventures of Batman')
#print(mo1.group())
#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())
#mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group())