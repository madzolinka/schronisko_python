class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} lat)"

    def __eq__(self, other):
        return isinstance(other, Animal) and self.name == other.name and self.species == other.species


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Pies")
        self.breed = breed

    def __str__(self):
        return f"Pies: {self.name}, rasa: {self.breed}, wiek: {self.age} lat"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Kot")
        self.color = color

    def __str__(self):
        return f"Kot: {self.name}, kolor: {self.color}, wiek: {self.age} lat"