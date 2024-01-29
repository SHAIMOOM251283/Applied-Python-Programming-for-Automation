import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'\.')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))


#dotRegex = re.compile(r'\.')
#atRegex = re.compile(r'.at')
#text = 'The cat in the hat sat on the flat mat.'
# Match a literal dot
#matches_dot = dotRegex.findall(text)
#print("Matches for literal dot:", matches_dot)
# Match any character followed by 'at'
#matches_at = atRegex.findall(text)
#print("Matches for .at pattern:", matches_at)


#atRegex1 = re.compile(r'.at')
#atRegex2 = re.compile(r'\.')
#print(atRegex1.findall('The cat in the hat sat on the flat mat.'))
#print(atRegex2.findall('The cat in the hat sat on the flat mat.'))





