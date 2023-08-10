## Operasi

# index  0(-3)  1(-2)     3(-1) 
data = ["ucup", "Otong", "Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manu=ipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"data sesudah di tambah \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi =\n{data}")
data_baru = ["Ujang", "Asep", "Agaton"]

# menambah list dengan list
data_baru = ["ujang", "usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah =\n{data}")

#meremove data
data.remove("ujang")
# data.remove("usep" akan error karena hurufnya tidak sesuai)

# meremove data paling belakang
data.pop()
print(f"data akhir =\n{data}")

print(data)



