import requests

def choose_1():
  Key = '5e1cc66c673efde5f70d0e7b5eee0adc'
  masukan=input("Masukkan Nama Kota : ")#masukkin nama kota
  Cat= f'/cities?q={masukan}&count=5'
  total_resto = int(input('Masukan jumlah resto yg ingin ditampilkan:'))
  Host='https://developers.zomato.com/api/v2.1'

  HeadInfo={"user-key":Key}

  url=Host+Cat

  data=requests.get(url,headers=HeadInfo)

  output=data.json()

  #nampilin id
  kategori=output['location_suggestions'][0]['id']
  kategori = str(kategori)
  print(kategori)
  #nama_restoran="https://developers.zomato.com/api/v2.1/search?entity_id={kategori}&entity_type=city"
  nama_restoran = f'/search?entity_id={kategori}&entity_type=city'
  HeadInfo={"user-key":Key}
  #nama restoran di daerah tertentu , harus dipake loop sepanjang list nya
  url1=Host + nama_restoran

  data1=requests.get(url1,headers=HeadInfo)

  output1=data1.json()
  nama=[]
  establishment = []
  cuisine=[]
  address = []
  phone = []
  rating = []
  review_count = []
  #i=int(input("Masukkan Jumlah Restoran yang akan ditampilkan : "))
  for i in range(len(output1['restaurants'])):
    nama.append(output1['restaurants'][i]['restaurant']['name'])
    establishment.append(output1['restaurants'][i]['restaurant']['establishment'])
    cuisine.append(output1['restaurants'][i]['restaurant']['cuisines'])
    address.append(output1['restaurants'][i]['restaurant']['location']['address']) #aggregate_rating
    rating.append(output1['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']) #aggregate_rating
    phone.append(output1['restaurants'][i]['restaurant']['phone_numbers']) #phone
    review_count.append(output1['restaurants'][i]['restaurant']['all_reviews_count'])
  print(len(nama))

  print('----')
  print(len(cuisine))

  for i in range(0, total_resto):
    print('Nama restoran: ')
    print(output1['restaurants'][i]['restaurant']['name'])
    print('Establishment:')
    if not establishment[i]:
      print('-')
    else:
      print(output1['restaurants'][i]['restaurant']['establishment'][0])
    print('alamat: ')
    print(output1['restaurants'][i]['restaurant']['location']['address'])
    print('Jenis restoran: ')
    print(output1['restaurants'][i]['restaurant']['cuisines'])
    print('No telepon: ')
    print(output1['restaurants'][i]['restaurant']['phone_numbers'])
    print('rating restoran: ')
    print(output1['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
    print('Total review: ')
    print(output1['restaurants'][i]['restaurant']['all_reviews_count'])

def choose_2():
  input_resto = input('Masukan nama resto yg ingin ditampilkan:')
  input_resto = input_resto.lower()
  input_city = input('Masukan nama Kota:')
  total_resto = int(input('Masukan jumlah menu yg ingin ditampilkan:'))
  Key = '8b391975206f15590caca03f62a67184'
  Cat = f'/cities?q={input_city}&count=5'
  Host = 'https://developers.zomato.com/api/v2.1'
  HeadInfo = {"user-key" : Key}
  url = Host + Cat
  data = requests.get(url, headers = HeadInfo)
  Output = data.json()
  kategori = Output['location_suggestions']
  cit_id = Output['location_suggestions'][0]['id'] 
  cit_id = str(cit_id)
  Cit = f'/search?entity_id={cit_id}&entity_type=city&q={input_resto}' 
  url2 = Host + Cit
  data2 = requests.get(url2, headers = HeadInfo)
  Output2 = data2.json()
  print(Output2)
  listresto = []
  idresto = []
  print('')
  if (Output2['results_found'] > 0): 
    for i in range (0,Output2['results_found']):
      searched_resto = Output2['restaurants'][0]['restaurant']['name'].lower() 
      print(searched_resto)
      if (searched_resto == input_resto.lower()):
        listresto.append(Output2['restaurants'])
        for j in range(0,total_resto):
          idresto.append(listresto[0][j]['restaurant']['R']['res_id'])
        break
      elif (idresto == []):
        print('Not Found')
  else:
    print('Not Found')
  print(idresto)
  for i in idresto:
    idreslink = f'/dailymenu?res_id={i}'
    url3 = Host + idreslink
    data3 = requests.get(url3, headers = HeadInfo)
    Output3 = data3.json()
    print(Output3)
    if (Output3['code'] == 200):
      print('Daily menu: ', Output3)
    else:
      print('No Menu Available, id:', i)

opt = input('\n1. Cari Resto \n2. Dialy Menu \nPilih Opsi 1-3:')
opt = int(opt)
if (opt == 1):
  choose_1()
elif (opt == 2):
  choose_2()
else:
  print('Error')