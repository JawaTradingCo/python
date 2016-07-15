import bs4
import requests
import re

domain = ""
c = 1
ulinks = []

def scrapePage(url):
	global c, domain, ulinks
	print("------"+url+"--------")
	r  = requests.get(url)

	soup = bs4.BeautifulSoup(r.text)



	for link in soup.select('a'):
		h = link.get('href')
		if h:
			if not h in ulinks and not "#" in h and not "mailto" in h and not "?" in h:
				ulinks.append(h)
				pattern  = re.compile(r'('+domain+')')
				print(str(c) + ") " + h)
				c += 1
				if c > 200:
					# stop at 200 links
					break
				if re.search(pattern,h):
					scrapePage(h)
		
	
		



if __name__ == '__main__':
	url = raw_input("Enter a website to extract the URL's (exclude http/s and www and slashes): ")
	domain = url
	scrapePage("http://"+url)
