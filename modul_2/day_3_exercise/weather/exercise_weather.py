##### Latihan Aplikasi Ramalan Cuaca
# Prakiraan Cuaca 
# input : Masukkan Nama Kota : 
# Output nya :

# Kota Yang Anda Pilih : .... 
# Suhu : .... (Celcius)
# Keadaan cuaca :  'Berawan'
# Koordinat Kota Anda : lat - long 
# Humidity Level : ...
# Kecepatan Angin : ....

# Kalau kota tidak ada :
# Keluar Notif : Kota Yang Anda masukkan tidak terdaftar
### Gunakan API openweather

#cara ngecek ada di word nya ga
#keyss={'apa','gimana','dan','dimana'}
#masuk=input()
#if masuk in keyss:
#    print("ada")

import requests

while True:
    key='32ceac9188b4a15e859b90dd2e5b3e0d'
    host="api.openweathermap.org"
    kota=input('Masukkan Nama Kota : ')
    nama_kotaa=kota.capitalize()

    try:
        nama_kota=str(nama_kotaa)
        url=f"http://{host}/data/2.5/weather?q={nama_kota}&appid={key}"
        data=requests.get(url)
        output=data.json()
        if nama_kota in output['name']:
            print(f'Kota Yang Anda Pilih : {nama_kota}')
            print(f"Suhu : {(output['main']['temp'])-273.15}")
            print(f"Keadaan Cuaca : {output['weather'][0]['main']}")
            print(f"Koordinat Kota Anda : {output['coord']['lat']} - {output['coord']['lon']}")
            print(f"Humidity Level : {output['main']['humidity']}")
            print(f"Kecepatan Angin : {output['wind']['speed']}")
            break
        else:
            print("Kota Yang Anda masukkan tidak terdaftar")
    except ValueError:
        print(nama_kota)
        print("Kota Yang Anda masukkan tidak terdaftar")

#print(output)
#print(output['main']['temp'])
#print(output['name'])