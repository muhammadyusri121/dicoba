# sdsjfhrsejgjighuir hyuithut ih uighduighui
print("Hello World")
print("Hello World")

# membuat program kasir
# 1. input nama barang
# 2. input harga barang
# 3. input jumlah barang
# 4. hitung total harga
# 5. tampilkan total harga
# 6. input uang
# 7. hitung kembalian
# 8. tampilkan kembalian
# 9. tampilkan terimakasih

print("Program Kasir")
nama_barang = input("Masukkan nama barang: ")
harga_barang = int(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = harga_barang * jumlah_barang
print("Total harga: ", total_harga)
uang = int(input("Masukkan uang: "))
kembalian = uang - total_harga
print("Kembalian: ", kembalian)
print("Terimakasih")