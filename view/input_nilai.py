from model import daftar_nilai

data = daftar_nilai.Data_mahasiswa()

def nilai():
        print("Input Nilai")
        print("="*15)
        input_nama = input("Masukan Nama   : ")
        if input_nama in data.nama:
            index = data.nama.index(input_nama)
            data.uts[index]     = int(input("Nilai UTS      : "))
            data.uas[index]     = int(input("Nilai UAS      : "))
            data.tugas[index]   = int(input("Nilai Tugas    : "))

            print("\nData nilai berhasil di input!")
        else:
            print("NAMA {0} TIDAK ADA! / ANDA BELUM MENAMBAH DATA".format(input_nama))

