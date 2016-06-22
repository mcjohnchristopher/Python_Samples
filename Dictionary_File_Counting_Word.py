# From a line
count = dict()
print 'Enter a line of text:'
line = raw_input()

words = line.split()
print 'Words'.words

for word in words :
	count = count.get(word,0)+1
print 'Totalcount:' count

# From a file

name = raw_input('Enter a file name:')
handle = open(name,'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	count = count.get(words,0)+1

bigcount = None
bigword = None
for word,count in count.items()
	if bigcount is None or count > bigcount:
		bigcount = count
		bigword = word

print bigword,bigcount