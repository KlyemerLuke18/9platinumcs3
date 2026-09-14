class CarInformation:
    def __init__(self, carBrand: str, yearCreation: int, carValue: int, performance: str):
        self.carBrand = carBrand
        self.yearCreation = yearCreation
        self.performance = performance
        self.__carValue = carValue
        self.speed = 0
    def drive(self, speed: int):
        if speed >= 0:
            self.speed = speed
    def setValue(self, newValue: int):
        if newValue >= 0:
            self.__carValue = newValue
    def getValue(self) -> int:
        return self.__carValue
    def getInfo(self) -> str:
        return f"{self.yearCreation} {self.carBrand} | Value: {self.__carValue} | Speed: {self.speed} km/h"
class Dealership:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.inventory = []
    def addCar(self, car: CarInformation):
        self.inventory.append(car)
    def displayInventory(self):
        print(f"\n{self.name} ({self.location}) Inventory")
        if not self.inventory:
            print("No cars in inventory.")
            return
        for v, car in enumerate(self.inventory, 1):
            print(f"{v}. {car.getInfo()}")

if __name__ == "__main__":
    print("\nBefore Relationship:")
    print()
    dealership = Dealership("Joogie Auto Group", "Goa, Camarines Sur")
    car1 = CarInformation("Toyota", 2020, 20000, "Reliable")
    car2 = CarInformation("Porsche", 2023, 120000, "High Performance")
    car3 = CarInformation("Honda", 2021, 22000, "Fuel Efficient")
    print(f"Dealership Created: {dealership.name}")
    print(f"Car 1 Created: {car1.getInfo()}")
    print(f"Car 2 Created: {car2.getInfo()}")
    print(f"Car 3 Created: {car3.getInfo()}")
    print("\nBuilding Relationship between Dealership and Cars...")
    dealership.addCar(car1)
    dealership.addCar(car2)
    dealership.addCar(car3)
    print("\nAfter relationship:")
    dealership.displayInventory()