from bs4 import BeautifulSoup
import requests

url='http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web=requests.get(url)

Out=BeautifulSoup(web.content,'html.parser')

import json
semua=[]
for i in Out.find_all('strong'):
    semua.append(i.text)

monster=semua[37:110]
ultraman=semua[2:36]
nums = []
num_monster = []
item = []
item_monster = []
for u in ultraman:
    d = str(u)
    nums.append(d[0:2])
    item.append(d[3:])

for m in monster:
    d = str(m)
    num_monster.append(d[0:2])
    item_monster.append(d[3:])

people = {"ultraman": {}, "monster": {}}
print(len(nums))
for i in range(0,len(nums)):
    people["ultraman"][nums[i]] = item[i]

for i in range(0,len(num_monster)):
    people["monster"][num_monster[i]] = item_monster[i]
hasil=[people]

with open("/Users/risyad/Desktop/code modul 2/farizzzzz.json","w") as f:
    json.dump(hasil,f)