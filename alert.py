import bs4
import requests
import time
import json
compare = ""
token = 'your token'

def monitor(url):
	global compare, token
	r  = requests.get(url)
	soup = bs4.BeautifulSoup(r.text)
	count = 1
	for text in soup.select('div.post'):
		if count == 1:
			if not compare:
				compare = text
			if text != compare:
				#change detected
				compare = text
				url = 'https://firespike.hipchat.com/v2/room/1005020/notification?auth_token=' + token
				payload = json.load(open("r.json"))
				headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
				r = requests.post(url, data=json.dumps(payload), headers=headers)
			count += 1
			time.sleep(60)
			#tick
			
		
if __name__ == '__main__':
	url = 'https://firespike.hipchat.com/v2/room/1005020/notification?auth_token=' + token
	payload = json.load(open("i.json"))
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	while True:
		monitor("http://www.dreamhoststatus.com/")
