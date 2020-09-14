#Input : 
#- Masukkan Nama Pokemon :

#Output :
#- Nama Pokemon : 
#- HP : 
#- Attack :
#- Defense :
#- Speed : 
#- Type : ....
#- URL : berisi url image foto pokemon 
#- Ability Name : 
#1 .....
#2 .....
#3 .....


from bs4 import BeautifulSoup
import requests

while True:
#Memanggil nama pokemon
    val=input("Masukkan Nama Pokemon ").lower()
    try:
        nama=str(val)
        url=f"https://pokeapi.co/api/v2/pokemon/{nama}"
        data=requests.get(url)
        output=data.json()
        hp=output['stats'][0]['base_stat']
        attack=output['stats'][1]['base_stat']
        defense=output['stats'][2]['base_stat']
        speed=output['stats'][3]['base_stat']
        print(f'Nama Pokemon : {nama}')
        print(f'HP : {hp}')
        print(f'Attack : {attack}')
        print(f'Defense : {defense}')
        print(f'Speed : {speed}')

        for x in output['types']:
            Type=x['type']['name']   
            print(f"Type Name : {Type}")

        url_pok=output['sprites']['front_default']
        print(f"URL : {url_pok}")

        for y in output['abilities']:
            Types=y['ability']['name']
            print(f"Ability Name : {Types}")
        break
    except ValueError:
        print("Nama Pokemon Tidak Terdapat")
