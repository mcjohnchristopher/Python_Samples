#example 1

total = 0
count = 0
while True:
	input =raw_input('Enter a number:')
	if input == 'done' : break
	value =float(input)
	total = total + value
	count = count + 1
avg = total/count
print 'Average', average

#example 2
numlist = list()
while True:
	input = raw_input('Enter a number:')
	if input == 'done' : break
	value = float(input)
	numlist.append(value)
avg = sum(numlist)/len(numlist)
print 'Average',avg