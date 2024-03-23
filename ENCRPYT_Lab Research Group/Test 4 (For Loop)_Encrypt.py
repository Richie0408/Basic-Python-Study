# Test 4
#     Tanyakan 3 hal kepada user : {Panjang}, {Lebar}, {Symbol}
#     Buatkan symbol tersebut menjadi sebuah persegi panjang sesuai dengan inputan panjang dan lebar
#     Jika inputnya seperti berikut: Panjang=2, Lebar=4, Symbol=$
#     Maka Outputnya : $$$$
#                      $$$$
           
Panjang = int(input("Masukkan Jumlah Panjang: "))
Lebar = int(input("Masukkan Jumlah Lebar: "))
Symbol = input("Masukkan Simbol: ")

for i in range(Panjang):
    output = ''
    for y in range(Lebar):
        output = output + Symbol
    print(output)


