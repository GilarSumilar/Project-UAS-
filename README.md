# Project-UAS

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Gilar Sumilar |
| **NIM** | 312210407 |
| **Kelas** | TI.22.A.4 |
| **Mata Kuliah** | Bahasa Pemrograman |

# UAS

#### Buatlah package dan modul dengan struktur seperti berikut:
- daftar_nilai.py berisi modul untuk:
tambah_data, ubah_data, hapus_data,
dan cari_data
- view_nilai.py berisi modul untuk:
cetak_daftar_nilai, cetak_hasil_pencarian
- input_nilai.py berisi modul untuk:
input_data yang meminta pengguna
memasukkan data.
- main.py berisi program utama (menu
pilihan yang memanggil semua menu
yang ada)

#### 1. `main.py` Berisi program utama dengan menu `menu = input("[(T)ambah, (I)nputNilai, (L)ihat, (C)ari, (H)apus, (U)bah, (K)eluar] : ")`

``` Python
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
```
#### Penjelasan 
Disini program utama ini terdapat modul yg berisi kode python `from view import input_nilai, view_nilai` &
`from model import daftar_nilai`. Modul memungkinkan Anda menulis kode yang terdiri dari beberapa file dan membaginya menjadi bagian-bagian yang lebih kecil, yang dapat diimport sesuai kebutuhan.

#### `input_nilai.py


