#Regular Expression
import re
hand = open('Filename.txt')
for line in hand:
	line =  line.rstrip()
	if re.search('From:',line):
	print line
	
# Without Regular Expression
hand = open('Filename.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:')>=0;
	print line