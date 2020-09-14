import requests
TOKEN = '4abSRLiQjyvJiSbT61SVXdBiv4oDIpTfHqwOcWOU'
BANK= input('Masukkan Nama bank ')
UANG= input('\nMasukkan Nama Mata Uang ')
nama_bank=BANK.lower()
nama_uang=UANG.lower()

url = f"https://api.kurs.web.id/api/v1?token={TOKEN}&bank={nama_bank}&matauang={nama_uang}"
data = requests.get(url)
output=data.json()
pilihan=int(input('\n1.idr to mata uang asing \n2.mata uang asing to idr\nPilih nomor '))
if pilihan==1:
    jumlah=float(input(f"\nMasukkan Nominal Uang Rupiah Anda "))
    hasil1=jumlah/output['jual']
    print(f"\nnilai uang anda {jumlah} rupiah, mempunyai nilai dalam {nama_uang} sebesar {hasil1}")
elif pilihan==2:
    jumlah=float(input(f"\nMasukkan Nominal Uang {nama_uang} Anda "))
    hasil2=jumlah*output['beli']
    print(f"\nnilai yang anda masukkan {jumlah} {nama_uang}, mempunyai nilai konversi sebesar {hasil2} rupiah")
    