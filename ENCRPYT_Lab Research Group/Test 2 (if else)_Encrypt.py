# Test 2
#     Buatkan program Currency Converter (Rupiah - USD)
#     Tanyakan 2 pertanyaan: {Uang} dan {Currency}
#     Print pesan seperti "Uang yang kamu punya adalah $10"
#     Maksimal 2 angka di belakang koma
#     Note -> 1 Dollar = 15000 Rupiah // Currencynya 2 pilihan (R)upiah/(D)ollar

Uang = int(input("Jumlah Uang: "))
print(Uang)
Currency = input("Currency (R)upiah/(D)ollard: ")

if Currency == "r":
    Currency_Dollar = Uang/15000
    print(f"Jumlah uang anda adalah ${round(Currency_Dollar,2)}")
elif Currency == "d":
    Currency_Rupiah = Uang*15000
    print(f"Jumlah uang anda adalah Rp{Currency_Rupiah}")
else: 
    print("Kode yang anda masukkan tidak valid, silahkan ulangi")

