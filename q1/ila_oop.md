## Sari-Sari Store Inventory System

#1. Encapsulation
Encapsulation can be applied by grouping each product’s related data (name, price, and quantity) together with the methods that operate on that data inside a single Product class. The attributes can be kept private (or protected) so that stock and price cannot be changed directly from outside the object; instead, controlled methods such as `updatePrice(), addStock(), and sellItem() are provided. This prevents accidental or invalid modifications (for example, setting a negative quantity) and keeps the product’s internal representation hidden. As a result, the program becomes more organized and safer because all product-related logic lives in one place rather than being scattered across many separate variables and functions.

class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def sell_item(self, amount):
        if amount <= self.__quantity:
            self.__quantity -= amount
            return True
        return False

    def get_info(self):
        return f"{self.__name}: ₱{self.__price} ({self.__quantity} left)"

#2. Abstraction
Abstraction can be used by defining a clear, simplified interface for working with products and the inventory without forcing the rest of the program to know the internal details. For example, a higher-level Inventory class can expose simple methods such as add_product(), sell(), and check_stock() while hiding how the products are actually stored (list, dictionary, or database). The store owner or other parts of the system only need to call these high-level operations. This improves design by reducing complexity: programmers can focus on what the inventory system does rather than how every detail is implemented, making the code easier to understand, maintain, and later extend.


class Inventory:
    def __init__(self):
        self.__products = {}   # internal storage is hidden

    def add_product(self, product):
        # details of how the product is stored are abstracted away
        self.__products[product.get_name()] = product

    def sell(self, name, amount):
        # caller does not need to know internal checks or data structure
        if name in self.__products:
            return self.__products[name].sell_item(amount)
        return False

#3. Inheritance
Inheritance can be applied by creating a general Product base class that contains common attributes and behaviors (name, price, quantity, sell_item(), etc.), then deriving specialized classes such as `PerishableProduct` or DiscountedProduct that inherit those features and add their own. A PerishableProduct might include an expiration date and a method to check whether the item is still good to sell, while a `DiscountedProduct` could override the price calculation. This avoids duplicating code for shared functionality and allows new product types to be introduced cleanly. The overall design becomes more scalable and organized because related product categories form a clear hierarchy instead of separate, nearly identical classes or long conditional statements.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

    def is_expired(self, current_date):
        return current_date > self.expiry_date

#4. Polymorphism
Polymorphism allows different product types to be treated uniformly through a common interface while still behaving in their own specialized ways. For example, both a regular Product and a DiscountedProduct can implement a get_price() method; when the inventory system calls get_price() on any product object, the correct version runs automatically (normal price or discounted price). The same method call can also be used when generating a sales report or calculating total inventory value. This improves the design by making the code more flexible and extensible, new product categories can be added later without rewriting the parts of the program that process products, because they all respond to the same method names.


class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount_rate):
        super().__init__(name, price, quantity)
        self.discount_rate = discount_rate

    def get_price(self):
        return self.price * (1 - self.discount_rate)

products = [
    Product("Sardines", 25.00, 50),
    DiscountedProduct("Soap", 40.00, 20, 0.15)
]

for p in products:
    print(f"{p.name}: ₱{p.get_price():.2f}")  # same call, different behavior


## Reflection
Among the four pillars, encapsulation would be the most useful for improving the sari-sari store inventory system. Because the store deals with many individual products that each have critical data (price and stock), protecting that data behind controlled methods prevents common errors such as negative quantities or unauthorized price changes. Encapsulation also keeps the product logic self-contained, which makes the program easier to maintain and less error-prone as the number of products grows. While the other pillars add valuable flexibility and organization, solid encapsulation provides the foundational safety and clarity that a practical inventory system needs first.