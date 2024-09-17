listMobil = [
    ['AB 1252 CD', 'Avanza', 250000], 
    ['AB 378 DE', 'Brio', 120000], 
    ['AB 1727 CE', 'Ertiga', 300000]
]


def main():
    while True:
        print("\nMenu:")
        print("1. Lihat data")
        print("2. Tambah data")
        print("3. Ubah harga")
        print("4. Hapus data")
        print("5. Sewa mobil")
        print("6. Keluar")

        inputan = input('Silahkan Pilih Menu (1/2/3/4/5/6): ')

        if inputan == '1':
            menuLihatData()
        elif inputan == '2':
            menuTambahData()
        elif inputan == '3':
            menuUbahData()
        elif inputan == '4':
            menuHapusData()
        elif inputan == '5':
            menuSewaMobil()
        elif inputan == '6':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")

def menuLihatData():
    while True:
        print("\nPilih opsi untuk menampilkan data:")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan nomor plat")
        print("3. Keluar")

        opsi = input("Masukkan pilihan (1/2/3): ")

        if opsi == '1':
            tampilkanSemuaData()
        elif opsi == '2':
            tampilkanBerdasarkanPlat()
        elif opsi == '3':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")

def menuTambahData():

    while True:
        print("\nPilih opsi untuk menambahkan data:")
        print("1. Tambah data")
        print("2. Keluar")
        
        opsi1 = input("Masukkan pilihan (1/2): ")

        if opsi1 == '1':
            tambahData()
        elif opsi1 == '2':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")


def menuUbahData():
    while True:
        print("\nPilih opsi untuk merubah data:")
        print("1. Ubah harga")
        print("2. Keluar")
        
        opsi1 = input("Masukkan pilihan (1/2): ")

        if opsi1 == '1':
            ubahData()
        elif opsi1 == '2':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")

def menuHapusData():
    while True:
        print("\nPilih opsi untuk merubah data:")
        print("1. Hapus data")
        print("2. Keluar")
        
        opsi1 = input("Masukkan pilihan (1/2): ")

        if opsi1 == '1':
            hapusData()
        elif opsi1 == '2':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")

def menuSewaMobil():
    while True:
        print("\nPilih opsi untuk menampilkan data:")
        print("1. Sewa mobil")
        print("2. Mobil tersewa")
        print("3. Keluar")

        opsi = input("Masukkan pilihan (1/2/3): ")

        if opsi == '1':
            sewaMobil()
        elif opsi == '2':
            lihatDataSewa()
        elif opsi == '3':
            break
        else:
            print("\nOpsi yang Anda masukkan tidak valid, silakan coba lagi.")


def tampilkanSemuaData():

    if not listMobil:
        print('\ntidak ada data.')
    else:
        print("\nData Mobil:")
        print(f'{'No Plat':<12} {'Merk Mobil':<15} {'Harga Sewa':<18}')
        for plat, merk, harga in listMobil:
            print(f'{plat:<12} {merk:<15} {harga:<18}')

def tampilkanBerdasarkanPlat():
    if not listMobil:
        print('\nData tidak ada.')
    else:
        platDicari = input("\nMasukkan nomor plat: ")
        dataDitemukan = False

        for plat, merk, harga in listMobil:
            if plat == platDicari:
                print('\nData Mobil:')
                print(f'{'No Plat':<12} {'Merk Mobil':<15} {'Harga Sewa':<18}')
                print(f'{plat:<12} {merk:<15} {harga:<18}')
                dataDitemukan = True
                break
        if not dataDitemukan:
            print(f"\nData dengan nomor plat {platDicari} tidak ditemukan.")



def tambahData():
    # list comprehension
    platTerdaftar = [mobil[0] for mobil in listMobil]
    platInput = input("\nMasukkan plat nomor mobil: ")
    if platInput in platTerdaftar:
        print("\nPlat mobil sudah terdaftar.")
    else:
        tipeMobil = input("\nMasukkan tipe mobil: ")
        hargaSewa = int(input("\nMasukkan harga sewa: "))
        while True:
            saveData = input('\nApakah anda ingin menyimpan data? (y/n): ')
            if saveData == 'y':
                listMobil.append([platInput, tipeMobil, hargaSewa])
                print(f"\nMobil dengan plat {platInput} berhasil ditambahkan dengan harga {hargaSewa}.")
                break
            elif saveData == 'n':
                break
            else:
                print('\nInput yang anda masukan salah.')
                continue


def ubahData():

    inputanPlat = input("\nMasukkan plat nomor mobil: ")

    found = False
    for mobil in listMobil:

        if mobil[0] == inputanPlat:
            print(f"\nMobil ditemukan: Plat: {mobil[0]}, Model: {mobil[1]}, Harga: {mobil[2]}")
            hargaBaru = int(input('\nSilahkan masukan harga baru: '))
            
            while True:
                melanjutkan = input('\nApakah anda ingin mengubah harga? (y/n): ')
                if melanjutkan == 'y':
                    mobil[2] = hargaBaru
                    print(f'\nHarga mobil dengan plat {mobil[0]} telah di ubah menjadi {mobil[2]}')
                    found = True
                    break
                elif melanjutkan == 'n':
                    print('Anda tidak jadi mengubah harga\nTerimakasih')
                    found = True
                    break
                else:
                    print('\nJawaban yang anda masukan salah.')
                    continue

    if not found:
        print("\nMobil dengan plat tersebut tidak ditemukan.") 


def hapusData():
    found = False
    inputanPlat = input("\nMasukkan plat nomor mobil: ")

    for mobil in listMobil:
        if mobil[0] == inputanPlat:
            while True:
                inputan = input(f'\nApakah anda ingin menghapus mobil dengan plat nomor {mobil[0]}? (y/n):')
                if inputan == 'y':
                    listMobil.remove(mobil)
                    print(f'\nMobil dengan plat nomor {mobil[0]} telah di hapus')
                    found = True
                    break
                elif inputan == 'n':
                    found = True
                    break
                else:
                    print('\nJawaban yang anda masukan salah')
                    continue
    if not found:
        print("\nMobil dengan plat tersebut tidak ditemukan.")

listSewa = []

def sewaMobil():
    platDicari = input("\nMasukkan nomor plat mobil yang ingin disewa: ")
    dataDitemukan = False

    for mobil in listMobil:
        if mobil[0] == platDicari:
            print(f"\nMobil ditemukan: {mobil[1]}, Harga sewa per hari: Rp {mobil[2]}")
            lamaSewa = int(input("Berapa hari ingin menyewa mobil ini?: "))
            while True:
                konfirmasi = input(f"\nApakah Anda yakin ingin menyewa mobil {mobil[1]} selama {lamaSewa} hari? (y/n): ")
                if konfirmasi == 'y':
                    totalHarga = mobil[2] * lamaSewa
                    listSewa.append([mobil[0], mobil[1], lamaSewa, totalHarga])
                    print(f"\nMobil dengan plat {mobil[0]} berhasil disewa selama {lamaSewa} hari. Total harga: Rp {totalHarga}")
                    dataDitemukan = True
                    break
                elif konfirmasi == 'n':
                    print('\nAnda tidak jadi menyewa mobil.')
                    dataDitemukan = True
                    break
                else:
                    print('\nAnda salah memasukan jawaban. Coba lagi')
                    dataDitemukan = True
                    continue
    
    if not dataDitemukan:
        print(f"\nMobil dengan plat {platDicari} tidak ditemukan.")

def lihatDataSewa():
    if not listSewa:
        print("\nBelum ada mobil yang disewa.")
    else:
        print("\nData Mobil yang Disewa:")
        print(f"{'No Plat':<12} {'Merk Mobil':<15} {'Lama Sewa (hari)':<18} {'Total Harga':<15}")

        for plat, merk, lama, total in listSewa:
            print(f"{plat:<12} {merk:<15} {lama:<18} {total:<15}")




main()