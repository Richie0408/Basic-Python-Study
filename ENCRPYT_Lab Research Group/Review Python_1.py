# #Python Numbers & Operator
# print(1+2)
# print(1-2)
# print(2*3)
# print(2**3)
# print(2/3)
# print(6//3)
# print(6%5)

# import math
# print(math.floor(2))

# #Python Text & String
# strings = "Halo semuanya"
# print(strings[0:-1])

# first = "Richie"
# last = "Cheristo"
# age = 19
# print(f'Halo, nama saya {first} {last}, sekarang saya berusia {age} tahun')

# name = 'richie cheristo'
# print(name.upper())
# print(name.replace('R','P'))

# #Input Value
# input("Masukkan nama anda ")

# #Test 1
#     #Tanyakan 3 pertanyaan: {Nama}, {Tempat Kuliah}, dan {Tahun Lahir}
#     #Print pesan seperti: Richie sekarang berusia 90 tahun dan sedang berkuliah di Telkom University

# Nama = input("Nama: ")
# Tempat_Kuliah = input("Tempat Kuliah: ")
# Tahun_Lahir = int(input("Tahun Lahir: "))
# Usia = 2024-Tahun_Lahir
# print(f'{Nama} sekarang berusia {Usia} dan sedang berkuliah di {Tempat_Kuliah}') 

# #===================================================================================================================================================

# #Conditional
# Panas = True
# Hujan = True
# if Panas:
#     print(
#         "Cuaca lagi panas\n"
#         "Banyak minum air ya"
#         )
# elif Hujan:
#     print(
#         "Hujannya deras banget loh\n"
#         "Jangan lupa sedia payung ya"
#     )
# else:
#     print(
#         "Cuacanya bagus hari ini, sejuk\n"
#         "Selamat menikmati hari"
#         )

# #Logical Operators
# Ganteng = True
# Banyak_Duit = False
# Mantan_Narapidana = False
# if Ganteng and Banyak_Duit and not Mantan_Narapidana:
#     print("Wah kamu cocok menjadi menantu saya")
# elif Ganteng or Banyak_Duit and not Mantan_Narapidana:
#     print("Wah agak gimana ya, tpi gpp, kamu masih layak untuk menjadi menantu saya")
# else:
#     print("PERGI KAMU SANA!!!, Jangan dekati putri saya lagi")

# # Test 2
# #     Buatkan program Currency Converter (Rupiah - USD)
# #     Tanyakan 2 pertanyaan: {Uang} dan {Currency}
# #     Print pesan seperti "Uang yang kamu punya adalah $10"
# #     Note -> 1 Dollar = 15000 Rupiah // Currencynya 2 pilihan (R)upiah/(D)ollar
# Uang = int(input("Jumlah Uang: "))
# Currency = input("Currency (R)upiah/(D)ollar: ")
# if Currency.upper == "R":
#     New_Currency = Uang/15000
#     print(f"Nilai uang anda adalah ${New_Currency}")
# elif Currency.upper == "D":
#     New_Currency = Uang*15000
#     print(f"Nilai uang anda adalah Rp{New_Currency}")
# else:
#     print("Ikuti arahan dari program, silahkan mengulangi")

# #===================================================================================================================================================
    
# #Looping
# #While Loop
# i = 1
# while 1<=5:
#     print(i)
#     i += 1
# print("Done")

# import random
# secret_number = random.randint(1,10)
# guess_now = 1
# guess_limit = 3
# while guess_now<=guess_limit:
#     print("Guess a number between 1-10")
#     guess = int(input(f"Guess {guess_now}: "))
#     guess_now += 1 
#     if guess == secret_number:
#         print('Congrats, You Win!!!')
#         break
#     else:
#         print('Nice Try')
# else:
#     print("You have run out your guess\n Try again later...")

command = ''
list = []
rest = False
eat = False

while True:
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
        print("Thank you for playing this game...")
    else:
        print("Sorry, i don't understand that code...\n")


        

        

    




# # For Loop
# for item in 'Ensyse':
#     print(item)

# prices = [10,20,30]
# total = 0
# for price in prices:
#     total+=price
# print(total)

# # Nested Loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')
 
# numbers = [5,2,5,2,2]

# for i in numbers:
#     output = ''
#     for y in range(i):
#         output += 'x'
#     print(output, end='')

# # Test 3
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

# #===================================================================================================================================================

# #Lists and The Method (append, insert, sort, remove)
# numbers = [3,6,2,8,9,10,14,12,11,15,15,3]
# max = numbers[0]
# for number in numbers:
#     if number>max:
#         max = number
# print(max)

# #Unpacking
# numbers = (1,2,3)
# print(numbers[0]*numbers[1]*numbers[2])
# x,y,z = numbers
# print(x*y*z)

#Dictionaries
# customer ={
#     "name" : "Richie Cheristo",
#     "age" : 20,
#     "is_verified" : True
# }



# #Test4
#     #Buatlah sebuah program yang berfungsi untuk menghapus angka duplikat pada list numbers di atas



# #===================================================================================================================================================

# #Function
# def salam_user(name):
#     print(f'Halo {name}')
#     return f"Halo {name}"
# salam_user("Richie")
# print(salam_user("Richie"))

# #Test 5
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
#             a = print(Symbol ,end='')
#         print("")
#     return a
# Panjang = int(input("Masukkan Jumlah Panjang: "))
# Lebar = int(input("Masukkan Jumlah Lebar: "))
# Symbol = input("Masukkan Simbol: ")
# pembuatan_kotak(Panjang, Lebar, Symbol)


#Harga 

