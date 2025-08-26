

# Base class (Parent)
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging... Battery life: {self.battery_life} hours")


# Derived class (Child) - Inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_type):
        super().__init__(brand, model, battery_life)  # inherit attributes
        self.strap_type = strap_type

    # Method overriding (Polymorphism)
    def call(self, number):
        print(f"{self.brand} {self.model} (Smartwatch) is making a quick call to {number}...")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 24)
watch1 = Smartwatch("Apple", "Watch 9", 18, "Silicone")

phone1.call("0712345678")
watch1.call("0798765432")  # Overridden method
phone1.charge()
watch1.charge()


# Activity 2: Polymorphism Challenge! 

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
