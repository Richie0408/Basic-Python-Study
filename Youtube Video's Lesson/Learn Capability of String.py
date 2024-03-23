course = 'Python for beginners'
print(course.upper())           #Kapitalkan
print(course.find('y'))         #untuk melihat ke urutan berapa y berada (0123dst)
print(course.replace('beginners','Advance Player\n'))
print('Pythn' in course)        #mengecek apakah python ada di course

###Arithmetic Operation#
x = 4
x+=5
print(x)

###Comparison Operation#
z=3>9
print(z)

###Logical Operation#
price = 10
print(price > 9 and price < 90)
print("aku mau boker \n")
#or, and, not

###If Statement#
temperature = input("What is the temperature around your area? ")
temp = int(temperature)
if temp >35:
    print("owh, its a hot day ain't it")
    print("Don't forget to drink much water yeah")
elif temp >20:
    print("its a nice day")
elif temp >10:
    print("It's a bit cold")
else:
    print("It's pretty cold")

###while loop
i =  1
while i <= 5:
    print(i,'\n')
    i = i+1

###Lists
names = ["Richie","Della","Harry"] ##urutannya 0,1,2,3,4,dst
                                   ##urutan dari belakang -1,-2,-3,dst
names[1] = "Seline"
print(names[0:2])

###List Method
numbers = [1,2,3,4,5]
numbers.append(7)  #menambahkan ke belakang
numbers.insert(1, "bangke") #menambahkan ke urutan ke-1
numbers.remove (5)

print(len(numbers),'\n')

###For Loops
angka = [1,2,3,4,5,9]
for item in angka:
    print (item)

i = 0
while i < len(angka):
    print(angka[i])   ##bagian pusing ga paham
    i=i+1

###The Range () Function
angka_2 = range (5,10,2)
print(angka_2)
for angka_1 in range(2):
    print(angka_1,'\n')

for angka_1 in angka_2:
    print(angka_1)

###Tuples
angka_3 = (1,2,3,3)

print(angka_3.count(3))







