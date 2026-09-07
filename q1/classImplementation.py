class CarInformation:
    def __init__(self, carBrand: str, yearCreation: int, carValue: int, performance: str):
        self.carBrand = carBrand
        self.yearCreation = yearCreation
        self.performance = performance
        self.carValue = carValue  
        self.speed = 0

    def drive(self, speed: int):
        if speed >= 0:
            self.speed = speed

    def setValue(self, newValue: int):
        if newValue >= 0:
            self.carValue = newValue

    def get_info(self) -> str:
        """Returns car details including private value."""
        return f"{self.yearCreation} {self.carBrand} | Value: ${self.carValue} | Speed: {self.speed} km/h"


if __name__ == "__main__":
    car1 = CarInformation("Toyota", 2020, 20000, "Reliable")
    car2 = CarInformation("Porsche", 2023, 120000, "High Performance")

    print("\nBefore")
    print("Car 1:", car1.get_info())
    print("Car 2:", car2.get_info())

    car1.drive(80)
    car1.setValue(18000)

    print("\nAfter:")
    print("Car 1:", car1.get_info())