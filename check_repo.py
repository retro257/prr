import requests
from bs4 import BeautifulSoup as bs
import datetime
import threading

def get_agent():
	import random
	import re
    
	while True:
		file = open("useragents.txt")
		lines = file.readlines()
		s = lines[random.randint(0, len(lines)-1)][0:-1]
		
		if s == " ":
			continue
		if "Windows" not in s and "Linux" not in s:
			continue
		pat = r"Chrome/[\d]+"
		rt = re.findall(pat, s)
		
		if rt == []:
			continue
		ch_vers = rt[0][7:len(rt[0])]
		if int(ch_vers) < 75:
			continue
		
		return s

def check(url):

        file = open("new_repo.txt", "a+")
        
        header = {"user-agent": get_agent()}
        print("https://github.com"+url)
        page = requests.get("https://github.com"+url, headers=header)

        soup = bs(page.text, "html.parser")

        allNews = soup.findAll('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')
        if len(allNews) > 5:
            file.write(url+"\n")
            file.close()

        

while True:
    file = open("saved_urls.txt", "r")

    urls_sp = file.readlines()[0]
    urls = urls_sp.split(";")
    file.close()

    file = open("saved_urls.txt", "w")
    file.write("k")
    file.close()

    thread = 0

    for i in range(0, len(urls)):

        thread = threading.Thread(target=check, args=(urls[i],))
        
        thread.start()

    while True:
        if not thread.isAlive():

            
            break
