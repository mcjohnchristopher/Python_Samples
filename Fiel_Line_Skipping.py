fhand = open('File.txt')
for line in fhand():
	line = line.rstrip()
	#Skip Unintrested lines
	if not line.startswith('From:')
		continue
		# printing remaining line
		print line

fhand = open('file.txt')
for line in fhand:
	line = line.rstrip()
	if not '@.gmail.com' in line
		continue
	print line