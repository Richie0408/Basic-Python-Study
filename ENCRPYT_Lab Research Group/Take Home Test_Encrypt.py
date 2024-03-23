menu ={
    "nasi goreng" : 10,
    "ketoprak": 10,
    "teh obeng": 5,
    "ayam goreng": 20,
    "pizza": 50,
    "steak": 60,
    "kuku bima": 5,
}

pesanan = []
harga = 0
remover = []

print("======= Menu Hari Esok =======")


for key, value in menu.items():
    remover.append(f'-{key}')
    print(f"{key:15}: ${value}")


makanan = ''
while makanan != "s":
    makanan = input("Silahkan input pesanan anda (s jika selesai): ").lower()
    if makanan =="s":
        break
    elif menu.get(makanan) is not None:
        pesanan.append(makanan)
    elif makanan in remover:
        pesanan.remove(makanan[1:])
    else:
        print("menu tidak tersedia")

nasigoreng_count = 0
ketoprak_count = 0
tehobeng_count = 0
ayamgoreng_count = 0
pizza_count = 0
steak_count = 0
kukubima_count = 0


for item in pesanan:
    if item == "nasi goreng":
        nasigoreng_count+=1
    elif item == "ketoprak":
        ketoprak_count +=1
    elif item == "teh obeng":
        tehobeng_count +=1
    elif item == "ayam goreng":
        ayamgoreng_count +=1
    elif item == "pizza":
        pizza_count +=1
    elif item == "steak":
        steak_count +=1
    elif item == "kukubima":
        kukubima_count +=1
    harga = harga + menu.get(item)

pesanan =set(pesanan)
jumlah_jenis_pesanan = len(pesanan)

if harga >= 50:
    diskon = 20/100*harga
    if jumlah_jenis_pesanan >= 2:
        diskon+=10
        if diskon >= 50:
            diskon = 50
    else: 
        if diskon >= 30:
            diskon = 30
elif jumlah_jenis_pesanan >= 2:
    diskon = 10
else:
    diskon = 0

print("\n============ Nota Hari Esok ============")
print('-----------------------------------------')
for item in pesanan:
    if item == "nasi goreng":
        print(f'{item:15}: {nasigoreng_count} x ${menu.get(item):3}:  ${nasigoreng_count*menu.get(item)}')
    elif item == "ketoprak":
        print(f'{item:15}: {ketoprak_count} x ${menu.get(item):3}:  ${ketoprak_count*menu.get(item)}')
    elif item == "teh obeng":
        print(f'{item:15}: {tehobeng_count} x ${menu.get(item):3}:  ${tehobeng_count*menu.get(item)}')
    elif item == "ayam goreng":
        print(f'{item:15}: {ayamgoreng_count} x ${menu.get(item):3}:  ${ayamgoreng_count*menu.get(item)}')
    elif item == "pizza":
        print(f'{item:15}: {pizza_count} x ${menu.get(item):3}:  ${pizza_count*menu.get(item)}')
    elif item == "steak":
        print(f'{item:15}: {steak_count} x {menu.get(item):3}:  ${steak_count*menu.get(item)}')
    elif item == "kukubima":
        print(f'{item:15}: {kukubima_count} x {menu.get(item):3}:  ${kukubima_count*menu.get(item)}')
print(f'{" ":17} {"DISKON":3}:  ${diskon}')
print('-----------------------------------------')
print(f'{" ":13} {" HARGA JUAL":3}: ${harga}')
print('-----------------------------------------')
harga = harga-diskon
print(f'{" ":18} {"TOTAL":3}: ${harga}')



















