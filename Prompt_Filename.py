Fname = raw_input('Enter the fiel name')
fhand = open(Fname)
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1 
print 'There were', count ,subject lines in,fname		
		