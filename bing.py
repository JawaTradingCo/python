import bs4
import requests
import re
import os, urllib2
import ftplib



# image snagging script that takes a dictionary of search engine terms
# searches the page for anchors that contain an image
# creates a folder for categorization
# downloads the image if there is no error
# uploads it to an ftp destination

domain = ""
c = 1
ulinks = []
terms = ["cat","dog","puppy","kitten","rabbit","cute baby"]

def scrapePage(url):
	global c, domain, ulinks
	session = ftplib.FTP('ftp.example.com','username','password')
	session.cwd("python.firespike.com/images")
	for t in terms:
		if not os.path.exists(t):
			os.makedirs(t)
		
		q = url + t
		print("------"+q+"--------")
		r  = requests.get(q)

		soup = bs4.BeautifulSoup(r.text)

		for link in soup.select('a'):
			h = link.get('href')
			if h:
				if "http" in h and not "?" in h and ("jpg" in h or "png" in h):
					
					try: 
						print("\033[1;37;40m "+str(c) + ") " + h)
						img = urllib2.urlopen(h,timeout=5)
						temp = h.split("/")
						localFile = open(t+'/'+temp[-1],'wb')
						localFile.write(img.read())
						localFile.close()
						
						session.storbinary("STOR " + temp[-1], open(t+'/'+temp[-1], "rb"), 1024)
						
						
					except urllib2.HTTPError as error:
						print("\033[1;31;40m "+str(c) + ") [ERROR]" + h)
						
						
					except urllib2.URLError as error:
					    	print("\033[1;31;40m "+str(c) + ") [ERROR]" + h)
					     
					
					
					c += 1
				
		
	session.quit()
		



if __name__ == '__main__':
	url = "www.bing.com/images/search?q="
	
	scrapePage("http://"+url)
