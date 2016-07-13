num = [1,2,3]
num_sum = 0
count = 0
for x in num:
 num_sum = num_sum + x
 count = count + 1
 if count == 2:
   break
print (num_sum)
print (count)