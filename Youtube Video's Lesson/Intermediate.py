result = 0
anggota = 0
for i in range(2,100):
    if i%2 == 1:
        result += i
        anggota += 1
print("Total : ", result)
print("Average : ", result/anggota)