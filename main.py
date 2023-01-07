from view import input_nilai, view_nilai
from model import daftar_nilai

data = daftar_nilai.Data_mahasiswa()

print("="*20)
print("|PROGRAM INPUT DATA|")
print("="*20)

while True: 
    print()
    menu = input("[(T)ambah, (I)nputNilai, (L)ihat, (C)ari, (H)apus, (U)bah, (K)eluar] : ")
    print("~"*78)
    print()

    if menu.lower() == 't':
        data.tambah()


    elif menu.lower() == "i":
        input_nilai.nilai()


    elif menu.lower() == 'l':
        if data.nama:
            view_nilai.lihat()
        else:
            print("BELUM ADA DATA!, pilih [T/t] untuk menambah data")  

    elif menu.lower() == 'c':
        if data.nama:
            data.cari()
        else:
            print("BELUM ADA DATA!, pilih [T/t] untuk menambah data") 
            

    elif menu.lower() == "h":
        data.hapus(data.nama)


    elif menu.lower() == "u":
        data.ubah(data.nama) 

    elif menu.lower() == "k":
        print("Program selesai, Terima Kasih :) ")
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/L/I/H/U/K] untuk menjalankan program!".format(menu))