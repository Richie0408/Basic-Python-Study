i = int(input ("How many test? "))
y = 1

while y<=i:
    angka_n = int(input("> "))
    angka_1 = int(input("> "))
    angka_2 = int(input("> "))
    angka_3 = int(input("> "))
    angka_4 = int(input("> "))

    data_range_1 = list(range(angka_1, (angka_n + 1), angka_1))
    data_range_2 = list(range(angka_2, (angka_n + 1), angka_2))
    data_range_3 = list(range(angka_3, (angka_n + 1), angka_3))
    data_range_4 = list(range(angka_4, (angka_n + 1), angka_4))

    print(data_range_1)

    data_total = data_range_1 + data_range_2 + data_range_3 + data_range_4
    data_total = list(set(data_total))
    print (angka_n)
    print(angka_1,angka_2,angka_3,angka_4)
    print("Case #",y,":",len(data_total))
    y+=1
print("DONE")




