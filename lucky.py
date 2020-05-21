#! /usr/bin/python3
import sys
import webbrowser 
import requests
import bs4 


print("Baiduing...")
res = requests.get("https://www.baidu.com/s?wd=" + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    linkElems = soup.select(".r a")
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open("https://www.baidu.com" + linkElems[i].get('href'))
except Exception as exc:
    print(f"There was a problem {exc}.")