fhand = (romeo.txt)
counts = dict()
for line in fhand:
	words = line.split()
	for word in words():
		count word = count.get(word, 0) + 1

st = list
for Key,Value in count.items():
	st.append((val,key))

st.sort(reverse = true)
for val,key in st[:10]:
	print key, val
	
#Using Sorted Function
sorted [(v,k) for k,v in c.items()]: