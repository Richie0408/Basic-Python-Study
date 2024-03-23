phone = input("Phone: ")
perubahan_angka = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}
output = ""

for i in phone:
    output += perubahan_angka.get(i,"!")+ " "
print(output)



message = input("> ")
words = message.split(' ')
dictionary = {
    ":v" : "SIUUU",
    ":)" : "Ehe"
}
output_1 = ""
for x in words:
    output_1 += dictionary.get(x, x) + " "
print(output_1)


