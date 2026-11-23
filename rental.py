
# =====================================
# PROJECT UTS PEMROGRAMAN BERORIENTASI OBJEK
# SISTEM RENTAL KENDARAAN
# =====================================


# CLASS 1: KENDARAAN
class Kendaraan:
    jumlah_kendaraan = 0

    def __init__(self, kode, nama, jenis, harga):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.__status = "Tersedia"

        Kendaraan.jumlah_kendaraan += 1

    # Encapsulation dan property
    @property
    def status(self):
        return self.__status

    # Setter
    @status.setter
    def status(self, status_baru):
        if status_baru in ["Tersedia", "Disewa"]:
            self.__status = status_baru
        else:
            print("Status tidak valid!")

    # Class Method
    @classmethod
    def total_kendaraan(cls):
        return cls.jumlah_kendaraan

    # Static Method
    @staticmethod
    def validasi_harga(harga):
        return harga > 0

    # Method menampilkan kendaraan
    def tampilkan_data(self):
        print("--------------------------------")
        print("Kode Kendaraan :", self.kode)
        print("Nama Kendaraan :", self.nama)
        print("Jenis          :", self.jenis)
        print("Harga Rental   : Rp", self.harga)
        print("Status         :", self.status)


# CLASS 2: RENTAL
class Rental:
    def __init__(self, nama_pelanggan):
        self.nama_pelanggan = nama_pelanggan
        self.daftar_kendaraan = []

    # Menambahkan kendaraan
    def tambah_kendaraan(self, kendaraan):
        self.daftar_kendaraan.append(kendaraan)

    # Menampilkan kendaraan
    def tampilkan_kendaraan(self):
        print("\n=== DAFTAR KENDARAAN ===")

        for kendaraan in self.daftar_kendaraan:
            kendaraan.tampilkan_data()

    # Menyewa kendaraan
    def sewa_kendaraan(self, kode, lama):
        for kendaraan in self.daftar_kendaraan:
            if kendaraan.kode == kode:
                if kendaraan.status == "Tersedia":
                    if lama > 0:
                        total = kendaraan.harga * lama
                        kendaraan.status = "Disewa"

                        print("\n=== BUKTI PENYEWAAN ===")
                        print("Pelanggan :", self.nama_pelanggan)
                        print("Kendaraan :", kendaraan.nama)
                        print("Lama Sewa :", lama, "hari")
                        print("Total Biaya: Rp", total)
                        print("Status    : Berhasil disewa")
                        return
                    else:
                        print("Lama sewa harus lebih dari 0!")
                        return
                else:
                    print("Kendaraan sedang disewa!")
                    return

        print("Kode kendaraan tidak ditemukan!")

    # Mengembalikan kendaraan
    def kembalikan_kendaraan(self, kode):
        for kendaraan in self.daftar_kendaraan:
            if kendaraan.kode == kode:
                if kendaraan.status == "Disewa":
                    kendaraan.status = "Tersedia"
                    print("Kendaraan berhasil dikembalikan!")
                    return

                print("Kendaraan belum disewa!")
                return

        print("Kode kendaraan tidak ditemukan!")


# =====================================
# PROGRAM UTAMA
# =====================================

# Membuat object kendaraan
mobil = Kendaraan("K001", "Toyota Avanza", "Mobil", 350000)
motor = Kendaraan("K002", "Honda Vario", "Motor", 100000)
mobil2 = Kendaraan("K003", "Toyota Innova", "Mobil", 500000)

# Membuat object rental
rental = Rental("Andi Saputra")

# Memasukkan kendaraan ke sistem
rental.tambah_kendaraan(mobil)
rental.tambah_kendaraan(motor)
rental.tambah_kendaraan(mobil2)


# Menu program
while True:
    print("\n================================")
    print("       SISTEM RENTAL KENDARAAN")
    print("================================")
    print("1. Tampilkan Kendaraan")
    print("2. Sewa Kendaraan")
    print("3. Kembalikan Kendaraan")
    print("4. Total Kendaraan")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        rental.tampilkan_kendaraan()

    elif pilihan == "2":
        rental.tampilkan_kendaraan()
        kode = input("\nMasukkan kode kendaraan: ")
        lama = int(input("Lama sewa (hari): "))
        rental.sewa_kendaraan(kode, lama)

    elif pilihan == "3":
        kode = input("Masukkan kode kendaraan: ")
        rental.kembalikan_kendaraan(kode)

    elif pilihan == "4":
        print("Jumlah kendaraan:",
              Kendaraan.total_kendaraan())

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem rental!")
        break

    else:
        print("Pilihan tidak tersedia!")
