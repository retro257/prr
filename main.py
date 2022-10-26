from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import time


url = "https://github.com/search?o=desc&q=stars%3A%3E1&s=updated&type=Repositories"

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

while True:
    header = {"user-agent":get_agent()}
    da = datetime.today()
    page = requests.get("https://github.com/search?l=&o=desc&q=created%3A"+str(da.year)+"-"+str(da.month)+"-"+str(da.day)+"+created%3A"+str(da.year)+"-"+str(da.month)+"-"+str(da.day)+"&s=updated&type=Repositories", headers=header)

    soup = bs(page.text, "html.parser")

    allNews = soup.findAll('a', class_='v-align-middle')
    saved_urls = open("saved_urls.txt", "r")
    urls_not = saved_urls.readlines()[0]
    
    urls = urls_not.split(";")
    saved_urls.close()
    
    saved_urls = open("saved_urls.txt", "a+")
    sv = open("sv.txt", "r")
    svv = sv.readlines()[0]
    sv_urls = svv.split(";")
    sv.close()
    sv = open("sv.txt", "a+")

    for i in range(0, 10):
        try:
            dictt = allNews[i]["href"]
            if dictt not in sv_urls:
                saved_urls.write(dictt+";")
                sv.write(dictt+";")
                print(dictt)
        except IndexError:
            None
    saved_urls.close()
    time.sleep(4)