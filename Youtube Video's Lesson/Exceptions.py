#try and except
try:
    age = int(input("Age: "))
    income = 20000/age
    print(age)
except ZeroDivisionError:
    print("Value Invalid")
except ValueError:
    print("Value Invalid")