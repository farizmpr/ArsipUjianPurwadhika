###################################################
###################################################
############### MONGODB SYNTAX ####################
###################################################
###################################################

#####untuk melihat isi database (how to see database)
show dbs


### untuk membuat atau menggunakan database (to use database)
use name_database #jika database sudah ada sebelumnya fungsi ini untuk mengaktifkan atau memilih database tersebut (if database exist, this function led you to choose the database)
#####jika database belum ada sebelumnya, sistem akan membuat database tersebut kemudian mengaktifkannya (iif database  doesnt exist, this function led you to actife the database)

#### untuk menghapus database (to delete database)
#pastikan sudah masuk dan memilih database yang akan dihapus (menggunakan query use) (make sure that you choose the database)

db.dropDatabase()

#### untuk membuat collections (to make collection)
db.createCollection("nama collection")

#### untuk menampilkan collection (this syntax is to show the collection inside the database)
show collections

##### untuk menghapus collection (to drop the database)
db.namaCollection.drop()

##### untuk membuat user (to create user)
db.createUser({
    user:"budi",
    pwd:"buditopsecret",
    roles:["readWrite"]
})
Roles ===> sudah built-in 

#### untuk melihat daftar user (to see the list of user)
show users

db.getUsers()

db.getUsers({showCredentials:true})

#### untuk memasukkan data ke dalam collection (to insert data to the collection)
db.namaCollection.insert({key/property:value})

db.Employee.insert({"nama":xxx,"usia":xx,"kota":xxx,"gaji":xxxxx}) #example

#### banyak data (many data)
db.namaCollection([
    {key/property:value},#data pertama (first data)
    {key/property:value},#data kedua (second data)
    {key/property:value}#data ketiga (third data)
])

### untuk melihat data isi dari collection (to see the data from collection)
db.namaCollection.find()

db.Employee.find()

db.Employee.find().pretty()### agar tampilan lebih bagus

#### untuk melihat data - isi collection dengan kondisi tertentu

db.namaCollection.find({kondisi})

db.Employee.find({"nama":xxx})### hanya menampilkan data yang memenuhi kriteria atau kondisi



####struktur dasar
db.namaCollection({},{})
{} pertama menunujukan data mana yang mau di update 
{} kedua data apa yang di update 
#########update seluruh property alias isinya
db.Employee.update({kondisi},{property update}) ====> data yang memenuhi kondisi semua property akan diubah menjadi sesuai property update

#######update property tertentu
db.Employee.update({kondisi},{$set:{property:valueUpdate}}) ==> data yang memenuhi kondisi, hanya property tertentu yang akan di update value nya


##### untuk ubah value tertentu 
db.Employee.update({kondisi},{$rename:{property:propertybaru}})

#### update seluruh data menjadi property tertentu
db.Employee.update({},{"lokasi":"jakarta"})====> seluruh data bakal berubah jadi lokasi jakarta

db.Employee.update({},{$set{property:valueUpdate}})


##### update seluruh data property tertentu (value)
db.Employee.update({},{$set{property:valueUpdate}})

##### update nama value tertentu 
db.Employee.update({},{$rename:{property:propertybaru}})

#####cara menghapus satu propery
db.Employee.update({"nama":"caca F"},{$unset:{"umur":true}})

#### menghapus satu data
db.Employee.remove({"nama":"caca F"})

######ketika akan mengupdate banyak data, query update, diubah menjadi updateMany

#### update seluruh data menjadi property tertentu
db.Employee.updateMany({},{"lokasi":"jakarta"})====> seluruh data bakal berubah jadi lokasi jakarta

db.Employee.updateMany({},{$set{property:valueUpdate}})


##### update seluruh data property tertentu (value)
db.Employee.updateMany({},{$set{property:valueUpdate}})

##### update nama value tertentu 
db.Employee.updateMany({},{$rename:{property:propertybaru}})

### menghapus property tertentu yang memenuhi kondisi
db.Employee.update({kondisi},{$unset:{namaProperty:true}})


db.Employee.update({"nama":"rani"},{$unset:{"usia":true}})==> akan menghapus usia di data rani

#### untuk menambahkan property baru ke data
db.Employee.update({kondisi},{$set:{property baru}})

db.Employee.update({"nama":"andi"},{$set{"gender":"male"}})===> akan menambahkan property gender ke data andi

##### untuk menghapus data tertentu
db.Employee.remove({kondisi})

db.Employee.remove({"nama":"caca F"})===>akan menghapus data caca

##### untuk menghapus keseluruhan data
db.Employee.remove({})=> menghapus data di seluruh collection employee


