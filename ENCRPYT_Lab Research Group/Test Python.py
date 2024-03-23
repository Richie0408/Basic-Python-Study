# Test 1
# Tanyakan 3 pertanyaan: {Nama}, {Tempat Kuliah}, dan {Tahun Lahir}
# Print pesan seperti: Richie sekarang berusia 90 tahun dan sedang berkuliah di Telkom University
# Nama = input("Nama: ")
# Tempat_Kuliah = input("Tempat Kuliah: ")
# Tahun_Lahir = int(input("Tahun Lahir: "))
# Usia = 2024-Tahun_Lahir
# print(f'{Nama} sekarang berusia {Usia} dan sedang berkuliah di {Tempat_Kuliah}') 

# Test 2
#     Buatkan program Currency Converter (Rupiah - USD)
#     Tanyakan 2 pertanyaan: {Uang} dan {Currency}
#     Print pesan seperti "Uang yang kamu punya adalah $10"
#     Maksimal 2 angka di belakang koma
#     Note -> 1 Dollar = 15000 Rupiah // Currencynya 2 pilihan (R)upiah/(D)ollar
# Uang = int(input("Jumlah Uang: "))
# Currency = input("Currency (R)upiah/(D)ollar: ")
# if Currency.lower() == "r":
#     New_Currency = Uang/15000
#     print(f"Nilai uang anda adalah ${round(New_Currency,2)}")
# elif Currency.lower() == "d":
#     New_Currency = Uang*15000
#     print(f"Nilai uang anda adalah Rp{round(New_Currency,2)}")
# else:
#     print("Ikuti arahan dari program, silahkan mengulangi")

# #Test 3
def game(command):
    print("============ WELCOME TO LIFE SIMULATOR ============\n"
          "press help to see all of the command")
    list = []
    rest = False
    eat = False
    while command != "quit":
        command = input("> ").lower()
        if command == "play":
            rest = False
            eat = False
            count = 0
            list.append(command)
            for x in list:
                if x == "play":
                    count+=1
            if count >= 3:
                print("Huh, i'm tired, i want to go home...\n")
            else:
                print("I'm so excited to play outside, here i go...\n")
        elif command == "rest":
            eat = False
            list.clear()
            if rest == False:
                print("I think i need to go to bed...\n")
                rest = True
            else:
                print("I'm not that tired to sleep.\n")
        elif command == "eat":
            rest = False
            list.clear()
            if eat == False:
                print("Argh, i want to eat baso ayam\n")
                eat = True
            else:
                print("I'm not hungry yet...\n")
        elif command == "help":
            print("========== Game Guide ==========\n"
                "play - to play outside\n" 
                "rest - to rest\n"
                "eat - to eat\n"
                "quit - to quit the game\n"
                "================================\n")
        elif command == "quit":
            print("Thank you for playing this game...\n")
            break
        else:
            print("Sorry, i don't understand that code...\n")
game('')

# # Test 4
# #     Tanyakan 3 hal kepada user : {Panjang}, {Lebar}, {Symbol}
# #     Buatkan symbol tersebut menjadi sebuah persegi panjang sesuai dengan inputan panjang dan lebar
# #     Jika inputnya seperti berikut: Panjang=2, Lebar=4, Symbol=$
# #     Maka Outputnya : $$$$
# #                      $$$$
           
# Panjang = int(input("Masukkan Jumlah Panjang: "))
# Lebar = int(input("Masukkan Jumlah Lebar: "))
# Symbol = input("Masukkan Simbol: ")
# for x in range(Panjang):
#     for y in range(Lebar):
#         print(Symbol ,end='')
#     print("")

# Test 5
# ibukota ={
#     "Alpro" : "Algoritma Pemrograman",
#     "TI" : "Teknik Industri",
#     "Gamtek" : "Gambar Teknik",
#     "sem": "semester",
#     "dua": 2
# }
# message = input("> ")
# words = message.split()
# output = ""
# for word in words:
#     output = output + ibukota.get(word,word)+" "
# print(output)

# #Test 6
#     #Buatkan kode di bawah ini menjadi Function yang reusable
#     # Panjang = int(input("Masukkan Jumlah Panjang: "))
#     # Lebar = int(input("Masukkan Jumlah Lebar: "))
#     # Symbol = input("Masukkan Simbol: ")
#     # for x in range(Panjang):
#     #     for y in range(Lebar):
#     #         print(Symbol ,end='')
#     #     print("")

# def pembuatan_kotak(Panjang, Lebar, Symbol):
#     for x in range(Panjang):
#         for y in range(Lebar):
#             print(Symbol ,end='')
#         print("")
#     return
# Panjang = int(input("Masukkan Jumlah Panjang: "))
# Lebar = int(input("Masukkan Jumlah Lebar: "))
# Symbol = input("Masukkan Simbol: ")
# print(pembuatan_kotak(Panjang, Lebar, Symbol))


# def kata_kunci_kuliah (message):
#     kuliah ={
#         "Alpro" : "Algoritma Pemrograman",
#         "TI" : "Teknik Industri",
#         "Gamtek" : "Gambar Teknik",
#         "sem": "semester",
#         "dua": 2
#     }
#     words = message.split()
#     output = ""
#     for word in words:
#         output = output + kuliah.get(word,word)+" "
#     return output

# message = input("> ")
# print(kata_kunci_kuliah(message))