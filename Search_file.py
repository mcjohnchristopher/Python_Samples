# With new line
Fhand = open('file.txt')
for line in fhand:
	if line.startswith('From:'):
		print line

#Remove #new line
Fhand = open('file.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print line
