import mylibdictionary


daftarBuah = {
    'Apel': [0, 'Apel', 20, 10000],
    'Jeruk': [1, 'Jeruk', 15, 15000],
    'Anggur': [2, 'Anggur', 20, 20000]
}

def main():
    listMenu = '''
Selamat Datang di Pasar Buah!'

List Menu:
1. Menampilkan Daftar Buah
2. Menambah Buah
3. Menghapus Buah
4. Membeli Buah
5. Exit Program
'''
    while True:
        # Menampilkan tampilan utama
        print(listMenu)

        # Meminta input nomor sesuai pilihan menu
        option = input("Masukkan angka sesuai menu: ")

        # Menjalankan fungsi sesuai pilihan menu
        if option == '1':
            mylibdictionary.show(daftarBuah)
        elif option == '2':
            mylibdictionary.add(daftarBuah)
        elif option == '3':
            mylibdictionary.delete(daftarBuah)
        elif option == '4':
            mylibdictionary.buy(daftarBuah)
        elif option == '5':
            break
        else:
            print('Input ada salah. Silahkan input ulang!')

# Menjalankan program utama
main()