#Klyemer Luke S. Colico                               #name                                            # comment                                        #this is a comment regarding the name                                #this is a comment regarding the comment regarding the name                    #this is a comment regarding the comment regarding the comment regarding the name
#9-Platinum                                           #grade & section 

# Main Class: Animal
class Animal:                                         #class animal creation
    def __init__(self, name):                         #defining the name
        self.name = name                              #setting name to name
    def make_sound(self):                             #defining the make_sound variable
        return self.make_sound                        #returning make_sound as make_sound
    def eat(self):                                    #defining eat
        return self.eat                               #returning eat at eat
# Child Class: Lion
class Lion(Animal):                                   #class lion creation
    def make_sound(self):                             #defining make_sound for lion
            return f"{self.name} roars loudly!"       #makes a message about lion roaring loudly
        def eat(self):                                #defining eat for lion
        return f"{self.name} eats fresh meat."        #makes a message about lion eats fresh meat
# Child Class: Elephant
class Elephant(Animal):                               #class elephant creation
    def make_sound(self):                             #defining make_sound for elephant
        return f"{self.name} trumpets!"               #makes a message about elephant trumpets
    def eat(self):                                    #defining eat for elephant
        return f"{self.name} eats grass and fruits."  #makes a message about elephant eats grass and fruits
# Child Class: Monket
class Monkey(Animal):                                 #class monkey creation
    def make_sound(self):                             #defining make_sound for monkey
        return f"{self.name} chatters!"               #makes a message about monkey chatters
    def eat(self):                                    #defining eat for monkey
        return f"{self.name} eats bananas."           #makes a message about monkey eats bananas
lion = Lion("Simba")                                  #gives a name to lion
elephant = Elephant("Dumbo")                          #gives a name to elephant
monkey = Monkey("George")                             #given a name to monkey
print(lion.make_sound())                              #prints Simba roars loudly!
print(lion.eat())                                     #prints Simba eats fresh meat.
print("-----")                                        #prints -----
print(elephant.make_sound())                          #prints Dumbo trumpets!
print(elephant.eat())                                 #prints Dumbo eats grass and fruits!
print("-----")                                        #prints -----
print(monkey.make_sound())                            #prints George chatters!
print(monkey.eat())                                   #prints George eats bananas!
print("-----")                                        #prints -----
