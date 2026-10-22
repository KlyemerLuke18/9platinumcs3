#Klyemer Luke S. Colico
#9-Platinum

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return self.make_sound
    def eat(self):
        return self.eat
class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!"
    def eat(self):
        return f"{self.name} eats fresh meat."
# Child Class: Elephant
class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"
    def eat(self):
        return f"{self.name} eats grass and fruits."
class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"
    def eat(self):
        return f"{self.name} eats bananas."
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")
print(lion.make_sound())
print(lion.eat())
print("-----")
print(elephant.make_sound())
print(elephant.eat())
print("-----")
print(monkey.make_sound())
print(monkey.eat())
print("-----")