class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 20
        self.energy = 20

    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("Woof!")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print("walking!")
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self


kalyb = Ninja("kalyb", "prince", "biscuits", True, Pet("woofy", "dog", "jump"))

kalyb.walk().walk()