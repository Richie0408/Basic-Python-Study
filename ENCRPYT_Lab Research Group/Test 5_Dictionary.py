# Test 5
katakunci_kuliah ={
    "Alpro" : "Algoritma Pemrograman",
    "TI" : "Teknik Industri",
    "Gamtek" : "Gambar Teknik",
    "sem": "semester",
    "dua": "2"
}
message = input("> ")
words = message.split()
output = ""
for word in words:
    output = output + katakunci_kuliah.get(word,word)+" "
print(f"{output}")