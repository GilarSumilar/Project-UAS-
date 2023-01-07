from model import daftar_nilai

data = daftar_nilai.Data_mahasiswa()

# Menampilkan seluruh data 
def lihat():
    for i in range(len(data.nama)):
        print(f"\nData ke -{i+1}")
        print(f"Nama Mahasiswa: {data.nama[i]}")
        print(f"NIM Mahasiswa : {data.nim[i]}")
        print(f"Nilai UTS     : {data.uts[i]}")
        print(f"Nilai UAS     : {data.uas[i]}")
        print(f"Nilai TUGAS   : {data.tugas[i]}")