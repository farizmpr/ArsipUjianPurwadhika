###################################################
###################################################
############### PYMONGO ###########################
###################################################
###################################################

import pymongo as p 
dburl='mongodb://localhost:27017'#mendefinisikan lokasi server lokal dan port yang digunakan
#27017 itu default

#definisikan client
myMongo=p.MongoClient(dburl) #mendefinisikan client yang terkoneksi dengan server yang sudah didefinisikan sebelumnya
#print("koneksi berhasil")

###step ini berhasil terus kita gaperlu pakai cmd 

#show database=> untuk melihat isi database dalam server
dbs = myMongo.list_database_names()
#print(dbs)

#untuk melihat collections, kita harus masuk/memilih database
myDB = myMongo['HRD'] ## memilih database
#myDB = myMongo['HRD'] #memilih database jika lebih dari 1

listCol=myDB.list_collection_names()#melihat nama collections

#print(listCol)

myCol=myDB['Employee']

#myCol1=myDB['Departemen'] ## contoh jika dalam database, ada banyak collection


#######melihat data dalam collection
#filter atau map
## hasil dari function.find() berupa oobject sehingga perlu dikonversi menjadi list agar terbaca
allData=list(myCol.find())
#print(allData)

###looping data yang tekah dikonversi
#for i in allData:
#    print(i)

##### opsi mengakses seluruh data
#-gunakan konversi
#-gunakan looping tanpa konversi

###looping data tanpa konversi
#for i in myCol.find():
#    print(i)


############ membuat database dan collections baru

newDB=myMongo['Penjualan']## tentukan nama database bary jika nama database sudah ada, dia akan akses data tersebut

newCol=newDB['karyawan']## membuat collections baru, ini berlaku juga jika mengakses database lama,
## tetapi collection baru atau belum ada di databasae

#### database tidak akan terbaca jika belum ada insert data ke dalam collection
#print(dbs)

##### memasukkan data ke dalam collection
##jika satu data, format data yang diinput menggunakan dictionary

data = {
    "nrp":"133ab",
    "nama":"fariz maulana purnomo",
    "kota":"jakarta",
    "usia":25
}

#newCol.insert_one(data)
#print("data submitted")

#print(dbs)

#for i in newCol.find():
#    print(i)

data1 = {
    "nrp":"133ab",
    "nama":"rosi",
    "kota":"bandung",
    "usia":23
}

#x=newCol.insert_one(data1)

#x.inserted_id => untuk memunculkan id ketika data awal baru dimasukkan

#print("data submitted, with id ", x.inserted_id)

#for i in newCol.find():
#    print(i)

#####akses data dengan kondisi tertentu
kondisi={"nama":"rosi"}
cari=newCol.find(kondisi)

#for i in cari:
#    print(i)

## db.karyawan.find({"nama":"rosi"})

###############memasukkan data berdasarkan user input
### memasukkan data satu input

Col_Baru = newDB['barang']### collection baru(barang), di dalam database penjualan(newDB)
'''
kode = input("masukkan kode barang : ")
nama = input("Masukkan nama barang : ")
harga = float(input("Masukkan harga barang : "))
stok = int(input("masukkan jumlah stok barang : "))

new_data = {
    "kode":kode,
    "nama":nama,
    "harga":harga,
    "stok":stok
}

x=Col_Baru.insert_one(new_data)
print("data submitted, with id ", x.inserted_id)

print("="*100)

print("keseluruhan data barang : ")

for i in Col_Baru.find():
    print(i)
'''

##### memasukkan banyak data sekaligus
'''
Col_2=newDB['seragam'] ### membuat collection baru(baru), di database lama (penjualan)

DATA=[
    {"jenis":"kemeja","stok":25},
    {"jenis":"celana panjang","stok":35},
    {"jenis":"kemeja","stok":25},
    {"jenis":"kaos","stok":15},
    {"jenis":"celana pendek","stok":20},
    {"jenis":"sepatu","stok":10}
]

Col_2.insert_many(DATA)

print("DATA BERHASIL DISIMPAN")
print("="*100)
for i in Col_2.find():
    print(i)
'''

######## mengakses data dengan kondisi tertentu

### beberapa data sesuai kondisi
nama=['kursi','bambu']
kondisi={"nama":{"$in":nama}}
#z=Col_Baru.find({"nama":{"$"}})

y=Col_Baru.find(kondisi)

#for i in y:
#    print(i)

########## conditional - logical condition

###operator or
#alt 1
#kondisi={
#    "$or":[
#        {"nama":"kursi"},
#        {"stok":5}
#    ]
#}

###alt 2
'''
opera="$or"
kon1={"nama":"kursi"}
kon2={"stok":5}
query={opera:[kon1,kon2]}

z=Col_Baru.find(query)

#for i in z:
#    print(i)
'''
### operator and

#alt 1
'''
kondisi1={"$and":[{"nama":"bambu"},{"stok":2}]}

z=Col_Baru.find(kondisi1)

for i in z:
    print(i)
'''


#######mengupdate data
Data={"kode":"003ab"}##kondisi data yang akan di update
new_val={"$set":{"stok":50}} ## value yang di update

Col_Baru.update_one(Data,new_val)

# db.Barang.update({},{})# query mongodb

print("data updated")

for i in Col_Baru.find(Data):
    print(i)


#####jika ingin update banyak data
Data={}
new_val={"$set":{"lokasi":"jakarta"}}

Col_Baru.update_many(Data,new_val)## untuk update banyak data

#### menghapus property
Data={"kode":"003ab"}##kondisi data yang akan di hapus
new_val={"$unset":{"stok":True}} ## property yang di update

Col_Baru.update_one(Data,new_val)# untuk menghapus property stok dari data kursi

#### mengubah nama property
Data={"kode":"003ab"}##kondisi data yang akan di diubah
new_val={"$rename":{"kode":"kodeBarang"}} ## mengganti nama property kode jadi kode barang

Col_Baru.update_one(Data,new_val)

####menghapus data
kondisi3={"nama":"bambu"}
Col_Baru.delete_one(kondisi3)### untuk menghapus data sesuai kondisi

####menghapus banyak data
kondisi4={}
Col_Baru.delete_many(kondisi4)

except ValueError
