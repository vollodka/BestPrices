from bs4 import BeautifulSoup
import re
import requests

url = "http://mysupermarket.org.ua/index.php?search=4820017000062"
headres = {
   "Content-Type": "text/html; charset=CP1251",
        "Referer": "http://mysupermarket.org.ua/index.php?search=4820017000062",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}


response = requests.get(url, headers=headres)


soup = BeautifulSoup(response.text)
kw = {"class": "list"}
res = soup.find("td", width="25%").findAll("p")
res = [str(x) for x in res if  "<a" in str(x)]

answer = []
for tag in res:
    answer.append({"price": float(re.findall('<b>(.*?) grn.</b>', tag)[0]),
                  'name': re.findall('<small>(.*?)</small>', tag)[0]})

print(answer)