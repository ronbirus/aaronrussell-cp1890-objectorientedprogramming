class Person:
    def __init__(self, name:str, age:int, pet:Dog
        self.name = name
        self.age = age
        self.pet = pet
    def walk_dog(self):
        dwalk = "Walked dog!"
        return dwalk
    def train_dog(self):
        dtrain = "Trained dog!"
        return dtrain
class Dog:
    def __init__(self, name:str, age:int, tricks: []):
        self.name = name
        self.age = age
        self.tricks = tricks
    def bark(self):
        bark = "ruff ruff!"
        return bark
    def sit(self):
        sit = "the dog sat"
        return sit
Aaron =Person(name = "Aaron Russell",
age = 24,
pet =Dog(Simmie))

Simmie = Dog(name = "Simmie",
age = 14,
tricks = ["sit", "fetch"])

