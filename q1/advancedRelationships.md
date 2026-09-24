# Advanced Class Relationships
# Klyemer Luke S. Colico

## Previous Work
* [Part I - Understanding Classes and Objects](classObjectUML.md)
* [Part II - Class Attributes and Methods](classAttributesMethods.md)
* [Part III - Class Relationships](classRelationships.md)

## Existing System Description
The previous system modeled a CarInformation class representing vehicle attributes and performance, connected to the Dealership class that managed inventory via a 1-to-many association.

## Inheritance Relationship
* **Parent Class:** CarInformation
* **Child Class:** ElectricCar
* **Explanation:** ElectricCar is a CarInformation. It inherits attributes such as carBrand, yearCreation, and performance from CarInformation, while adding specialized properties like batteryCapacity and an integrated BatterySystem.

## Inheritance UML
[Inheritance Diagram](images/inheritanceDiagram.png)

## Composition / Aggregation
* **Composition (Strong HAS-A):** ElectricCar has a BatterySystem. The BatterySystem object is created inside the ElectricCar constructor and its lifecycle is tied directly to the vehicle.
* **Aggregation (Weak HAS-A):** Dealership has a CarInformation. The dealership manages cars in its inventory list, but individual cars can exist outside of the dealership.

## Advanced UML Diagram
[Advanced Class Diagram](images/advancedClassDiagram.png)

## Python Implementation
[Python Code](advancedRelationships.py)

## Test Run
[Test Output](images/advancedTestRun.png)

## Object Diagram
[Object Diagram](images/advancedObjectDiagram.png)

## Reflection

### 1. Why did you choose your inheritance relationship?
I chose `lectricCar as a child of CarInformation because an electric car is a vehicle with all standard automotive properties (brand, year, driving capabilities), but requires specialized attributes like battery capacity.

### 2. How did inheritance reduce duplicate code?
Inheritance allowed `ElectricCar` to reuse carBrand, yearCreation, carValue, performance, and methods like drive() without re-declaring them. Reusing code via super().__init__() avoided redundant property initializations.

### 3. Why is your HAS-A relationship Composition or Aggregation?
The relationship between ElectricCar and BatterySystem is Composition because the battery system is instantiated directly within the car and cannot exist independently in the model. The Dealership to CarInformation relationship is Aggregation because vehicles exist as independent entities before being added to a dealership's inventory list.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
Association in Part III represented a generic connectivity line showing that Dealership holds CarInformation objects. Advanced relationships explicitly define lifetime ownership or hierarchical type of extension.

### 5. How does your design follow the DRY principle?
By placing common vehicle properties in CarInformation and delegating battery-specific tracking to BatterySystem, code duplication is eliminated across vehicle types, making the system modular and easy to maintain.

