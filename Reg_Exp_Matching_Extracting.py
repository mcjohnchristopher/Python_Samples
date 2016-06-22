import re
x = 'My 2 favorite numbers are 5 and 7'
y = re.findall('[0-9]+',x)
print y
y = re.findall('[AEIOU]+',x)
print y