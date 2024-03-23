class Point:
    def __init__(self, name, umur):
        self.name = name
        self.umur = umur
    def talk(self):
        print(f"hi, i am {self.name} and currently im {self.umur}")

richie = Point("Richie",19)
richie.talk()

