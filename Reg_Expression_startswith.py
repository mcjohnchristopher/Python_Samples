# Using Regular Expression
import re
hand = open('Filename.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From',line):
		print line
		
# Only python
hand = open('Filename.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:')
		print line