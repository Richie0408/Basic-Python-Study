x = int(input("Elevator 1 : "))
y = int(input("Elevator 2 : "))
z = int(input("Elevator 3 : "))

time = y-z
print(x,y,z)
t = y-x
if x<z<y:
    if t%2 == 0:
        print(time)
    else:
        print("-1")
else :
    print("-1")




