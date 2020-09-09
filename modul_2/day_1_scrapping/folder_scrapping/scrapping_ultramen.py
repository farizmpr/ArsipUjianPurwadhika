from bs4 import BeautifulSoup
import requests
import json

url='http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web=requests.get(url)

Out=BeautifulSoup(web.content,'html.parser')

#print(Out.p.text)
semua=[]
for i in Out.find_all('strong'):
    semua.append(i.text)
monster=semua[37:110]
ultraman=semua[2:36]

####cara fariz
monster1=[]
for x in monster:
    monster1.append(x.split(' ',1))
    print(monster1)
monster_fix = {i[0]:i[1] for i in monster1} 
#print(monster_fix)

ultraman1=[]
for x in ultraman:
    ultraman1.append(x.split(' ',1))
    print(ultraman1)
ultraman_fix = {i[0]:i[1] for i in ultraman1} 
#print(ultraman_fix)

tabelAkhir=[{'Ultraman':ultraman_fix},{'Monster':monster_fix}]
#print(tabelAkhir)

with open('/Users/risyad/Desktop/code modul 2/tabel_ultra.json','w') as file: #membuat kolom.json
     json.dump(tabelAkhir, file) #menulis file json
print("Data tersimpan")