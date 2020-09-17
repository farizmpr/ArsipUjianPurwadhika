###################################################
###################################################
############### MONGODB SYNTAX ####################
###################################################
###################################################

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


#### mendapatkan data dengan 2 atau lebih kondisi yang harus dipenuhi semua
db.Employee.find({$and:[{kondisi1},{kondisi2}]})====>2 kondisi harus bernilai tertentu

db.Employee.find({$and:[{"nama":"rani"},{"kota":"bandung"}]})==>akan menampilkan data yang namanya rani dan kotanya bbandung

#### mendapatkan data dua atau lebih kondisi yang harus dipenuhi salah satu
db.Employee.find($or:[{kondisi1},{kondisi2}])===> 2 kondisi yang harus dipenuhi salah satu

db.Employee.find({$or:[{"usia":20},{"gaji":12000000}}])===>menampilkan data yang usianya 20 atau gaji 12000000

#### mendapatkan data yang memiliki value kurang dari kondisi
db.Employee.find({property:{$lt:kondisi}})

db.Employee.find({"usia":{$lt:25}})===> akan menampilkan data yang memiliki usia dibawah 25

##### mendapatkan data yang memiliki value lebih dari kondisi
db.Employee.find({property:{$gt:kondisi}})

db.Employee.find({"gaji":{$gt:12000000}})===>akan menampilkan data yang memiliki gaji diatas 12000000

#### mendapatkan data yang memiliki value kurang dari sama dengan kondisi
db.Employee.find({property:{$lte:kondisi}})

db.Employee.find({"usia":{$lte:25}})====> akan menampilkan data yang memiliki usia kurang dari sama dengan 25

#### mendapatkan data yang memiliki value lebih dari sama dengan kondisi
db.Employee.find({property:{$gte:kondisi}})

db.Employee.find({"usia":{$gte:25}})====> akan menampilkan data yang memiliki usia lebih dari sama dengan 25

#### mendapatkan data teratas dengan jumlah tertentu

db.Employee.find().limit(jumlah)

db.Employee.find().limit(3)===> mengeluarkan 3 data teratas


### mendapatkan data terats dengan jumlah tertentu dengan skip(melewati data tertentu)

db.Employee.find().limit(jumlah).skip(jumlah)

db.Employee.find().limit(3).limit(2)==> akan mengeluarkan 3 data teratas , setelah melewati 2 data sebelumnya

### untuk mengurutkan data sorting

db.Employee.find().sort({property:1/-1})===>1 untuk ascending, -1 untuk descending

db.Employee.find().sort({"gaji":1})===> akan menampilkan gaji diurutkan dari yang terbesar ke terkecil

###untuk mengetahui jumlah data
db.Employee.find().count()

### untuk mengetahui jumlah data dengan kondisi tertentu
db.Employee.find({kondisi}).count

db.Employee.find({"nama":"andi"}).count====> akan menampilkan jumlah data yang memiliki nama andi

########################################################
########################################################
###############  MONGODB EXERCISE  #####################
########################################################
########################################################

1. use restoran
db.DataResto.find()

2. db.DataResto.find({},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1})

3. db.DataResto.find({},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})

4. db.DataResto.find({},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0,"address.zipcode":0})

5. db.DataResto.find({"borough":"Bronx"})

6. db.DataResto.find({"borough":"Bronx"}).limit(5)

7. db.DataResto.find({"borough":"Bronx"}).limit(5).skip(5)

8. db.DataResto.find({"grades":{$elemMatch:{"score":{$gt:90}}}})

9. db.DataResto.find({"grades":{$elemMatch:{"score":{$gt:90,$lt:100}}}})

10. db.DataResto.find({"address.coord":{$lt:-95.754168}})

11. db.DataResto.find({$and:[{"cuisine":{$ne:"American"}},{"grades.score":{$gt:70}},{"address.coord":{$lt:-65.754168}}]})

12. db.DataResto.find({"cuisine":{$ne:"American"},"grades.score":{$gt:70},"address.coord":{$lt:-65.754168}})

13. db.DataResto.find({"cuisine":{$ne:"American"},"grades.grade":{$ne:"A"},"borough":"Brooklyn"}).sort({"cuisine":-1})

14. db.DataResto.find( {name: /^Wil/}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } )

15. db.DataResto.find( {name: /ces$/}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } )

16. 

17. 

18. 

19. 

20. 

21. 

22. 

23. 

24. 

25. 