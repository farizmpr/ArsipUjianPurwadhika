from bs4 import BeautifulSoup
import requests

#json javasciprt object notation, format json itu di dalam list
member=[{
    'nama':'fariz',
    'usia':25,
    'kota':'bandung'
}]

import json

#menulis file json
#with open('member.json','w') as file:
#    json.dump(member,file)
#write=> untuk menulis file json
#read=> untuk membaca file json
#dump=> fungsi untuk menulis file json
#print('data tersimpan')

with open('member.json','r') as file:
    out=json.load(file)
print(out)

from bs4 import BeautifulSoup
ini = 'cobas.html'
Out=BeautifulSoup(open('/Users/risyad/Desktop/code modul 2/cobas.html','r'),'html.parser')

print(Out)
print(Out.prettify)

#print(Out.title)
#print(Out.tittle.text)

#print(Out.h1)
#print(Out.h1.text)

#print(Out.p)
#print(Out.p.text)

#print(Out.ul)
#print(Out.ul.text)

#if dan for
#for i Out.find_all('li'):
#    print(i)

#for i in Out.find_all('li',class_='Orang'):
#    print(i.text)

#tamu=[]
#for i in Out.find_all('li',class_='Orang'):
#    tamu.append(i.text)

#print(tamu)
#print(Out.a.text)


###ngambil online
#from bs4 import BeautifulSoup
#import requests

#url='http://127.0.0.1:5500/lat.html'
#web=requests.get(url)

#Out=BeautifulSoup(web.content,'html.paser')

#print(Out.tittle.text)

#for i in Out.find_all('li',class_='orang'):
#    print(i.text)

#for i in Out.find_all('li',id='person'):
#    print(i.text)


