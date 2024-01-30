import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
#(r 'Agent \w+') replaces both "Agent Alice" and "Agent Bob" with "CENSORED" in the input string.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#regular expression (r'Agent (\w)\w*')
#the sub method (r'\1***')