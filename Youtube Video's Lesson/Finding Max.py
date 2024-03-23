angka = [1,5,12,11,10]
max = angka[0]

for a in angka:
    if a > max:
        max = a
print(max)

x = input("Phone : ")

list_of_word = {
    "1": "One",
    "2": "Two",
}

output = ""

for y in x:
    output += list_of_word.get(y,"!") + " "
print(output)


j = input("> ")
k = j.split(' ')

dictionary= {
    "tod": "sahabatku",
    "kawan": "musuhku",
}
input = ""
for word in k:
    input += dictionary.get(word, word) + " "
print(input)
