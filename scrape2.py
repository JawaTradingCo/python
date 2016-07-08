import bs4
import requests

url = raw_input("Enter a website to extract the URL's from including http/s: ")

r  = requests.get(url)

soup = bs4.BeautifulSoup(r.text)

ulinks = []

for link in soup.select('a'):
	h = link.get('href')
	print h
	exists = 0
	for i in ulinks:
		if i == h:
			exists = 1
	if exists == 0:
		ulinks.append(h)
	
for i in ulinks:
	print i
