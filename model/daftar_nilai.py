class Data_mahasiswa:
    nama = []
    nim = []
    uts = []
    uas = []
    tugas = []

    # Tambah data
    def tambah(self):
        print("Tambah data\n")
        nama    = input("Nama           : ")
        self.nama.append(nama)
        nim     = int(input("NIM            : "))
        self.nim.append(nim)
        uts     = 0
        self.uts.append(uts)
        uas     = 0
        self.uas.append(uas)
        tugas   = 0
        self.tugas.append(tugas)

        print("\nData {0} berhasil di tambahkan".format(nama))
                
    # Menghapus inputan nama
    def hapus(self, nama):
        print("Hapus data inputan")
        nama = (input("\nMasukan Nama berdasarkan inputan : "))
        if nama in self.nama:
            print("Data {0} berhasil di hapus".format(nama))
            index = self.nama.index(nama)
            del self.nama[index]
            del self.nim[index]
            del self.uts[index]
            del self.uas[index]
            del self.tugas[index]
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
    
        # Mengubah data nama inputan
    def ubah(self, nama):
        input_nama = input("Nama yang ingin di ubah : ")
        if input_nama in nama:
            index = nama.index(input_nama)
            self.nim[index]     = int(input("NIM            : "))

            print("\nData {0} berhasil di ubah".format(input_nama))
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))
    
    def cari(self):
        print("Mencari data")
        print("="*15)
        nama = (input("\nMasukan Nama yg ingin di cari : "))
        if nama in self.nama:
            index = self.nama.index(nama)
            print(f"Nama Mahasiswa: {self.nama[index]}")
            print(f"NIM Mahasiswa : {self.nim[index]}")
            print(f"Nilai UTS     : {self.uts[index]}")
            print(f"Nilai UAS     : {self.uas[index]}")
            print(f"Nilai TUGAS   : {self.tugas[index]}")
        else:
            print("NAMA {0} TIDAK ADA!".format(nama))