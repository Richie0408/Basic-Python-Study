weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Weight in lbs: " + str(converted))
elif unit.upper() == "L":
    converted = float(weight) * 0.45
    print("Weight in Kgs: " + str(converted))
else:
    print("ERROR!!!")




