class Mammals:
    def walk(self):
        print("walk")

class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"{self.name} said : BARKBARKBARK")


class Cat:
    def miaw(self):
        print("MIAWMIAWMIAW")

dog1 = Dog("A dog named BOB")
dog1.bark()

cat1 = Cat()
cat1.miaw()