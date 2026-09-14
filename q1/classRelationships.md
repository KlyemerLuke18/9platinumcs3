# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
* **Class:** CarInformation
* **Description:** Represents a vehicle with brand, creation year, performance level, financial value, and current driving speed.

## New Related Class
* **Class:** Dealership
* **Description:** Represents an automotive business that holds, manages, and sells multiple vehicles in its inventory.


## Association
* **Relationship:** Dealership **manages / contains** CarInformation
* **Explanation:** A Dealership acts as a commercial location that stores and sells cars. It has a collection of CarInformation objects in their inventory.


## Multiplicity
* **Multiplicity:** 1 to 0...
* **Explanation:** A single Dealership can hold zero or many CarInformation vehicles in its inventory. Conversely, each specific CarInformation object is managed by exactly one Dealership.

## UML Class Relationship Diagram

[Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation

[View Python Source](classRelationships.py)

## Test Run

[Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram

[Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

The association between Dealership and CarInformation is a has-a relationship where a dealership contains and manages car objects in its inventory. The Dealership class acts as the aggregator, while CarInformation instances represent the inventory units. This relationship allows the dealership to query, list, and interact with the car data it holds.

### What multiplicity did you choose and why?

I chose a 1 to 0..* (one-to-many) multiplicity. This is appropriate because a dealership can start empty with zero cars or store many cars over time. Meanwhile, in this design, each specific car instance belongs to one specific dealership inventory.

### How did you implement the relationship in Python?

The relationship is implemented in Python by initializing a list attribute named self.inventory inside the Dealership __init__ constructor. The addCar() method takes an instance of CarInformation and appends it directly to the self.inventory list.

### Why did you store an object reference instead of copying its data?

Storing direct object references ensures data integrity and a single source of truth across the system. For example, if car1 updates its speed or value using car1.drive(80), accessing dealership.inventory[0] immediately reflects these changes without needing to manually update the dealership's records.

### If your relationship uses "many," why is a list appropriate?

A Python list is appropriate for a "many" relationship because it allows dynamic sizing, ordering, and easy iteration over multiple object references. The list stores memory references pointing to the actual CarInformation instances rather than plain strings, allowing methods to be invoked directly on list items during iteration.
