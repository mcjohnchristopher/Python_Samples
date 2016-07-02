import urllib
from BeautifulSoup import*

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#Retreive a list of anchor tags
#Each tag is like a dictionary of HTML attributes

tag = soup('a')

for tag in tags:
	print tag.get('href',None)