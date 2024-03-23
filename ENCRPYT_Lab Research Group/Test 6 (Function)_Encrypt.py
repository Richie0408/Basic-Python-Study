#Test 6
    #Buatkan kode di bawah ini menjadi Function yang reusable
    # Panjang = int(input("Masukkan Jumlah Panjang: "))
    # Lebar = int(input("Masukkan Jumlah Lebar: "))
    # Symbol = input("Masukkan Simbol: ")
    # for x in range(Panjang):
    #     for y in range(Lebar):
    #         print(Symbol ,end='')
    #     print("")

def pembuatan_kotak(Panjang, Lebar, Symbol):
    for x in range(Panjang):
        for y in range(Lebar):
            print(Symbol ,end='')
        print("")
    return
Panjang = int(input("Masukkan Jumlah Panjang: "))
Lebar = int(input("Masukkan Jumlah Lebar: "))
Symbol = input("Masukkan Simbol: ")
print(pembuatan_kotak(Panjang, Lebar, Symbol))


def kata_kunci_kuliah (message):
    kuliah ={
        "Alpro" : "Algoritma Pemrograman",
        "TI" : "Teknik Industri",
        "Gamtek" : "Gambar Teknik",
        "sem": "semester",
        "dua": 2
    }
    words = message.split()
    output = ""
    for word in words:
        output = output + kuliah.get(word,word)+" "
    return output

message = input("> ")
print(kata_kunci_kuliah(message))