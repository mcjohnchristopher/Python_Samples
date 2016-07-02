import urlib
fhand = urlib.urlopen('http://www.google.com/1.txt')
for line in fhand:
	words = line.strip()
		for word in words:
			counts[word] = counts.get(word, 0) + 1
print counts