#Klyemer Luke S. Colico
#9 - Platinum

#1.)
#a.What is duck typing, as explained in the video?
#Duck typing is a concept in Python where an object's suitability is determined by specific methods and behaviors rather than its class type

#b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?**
#The Car class needed to define a method with the exact same name as the method being called in the loop

#2.)
class Car:                                                        #creation of class Car
    def move(self):                                               #definition of method move for class Car
        print("The car drives on the road.")

class Boat:                                                       #creation of class Boat
    def move(self):                                               #definition of method move for class Boat
        print("The boat sails on water.")                         

class Drone:                                                      #creation of class Drone
    def move(self):                                               #definition of method move for class Drone
        print("The drone flies in the sky.")                      

def start_trip(vehicle):                                          #definition of function start_trip that takes a vehicle object as an argument
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)

#3.) How does the code in 2.2 demonstrate polymorphism?
#The code demonstrates polymorphism because in which a single function calls the same method name across three completely unrelated classes, Python automatically executes the behavior belonging to whichever object is passed into the function.
