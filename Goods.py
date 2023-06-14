class Property:
    def __init__(self, name, price):
        self.price = price
        self.name = name


class Car(Property):
    def __init__(self, name,  price, reward, for_poor=False):
        super().__init__(name, price)
        self.reward = reward
        self.for_poor = for_poor


class House(Property):
    def __init__(self, name,  price, reward, for_poor):
        super().__init__(name, price)
        self.reward = reward
        self.for_poor = for_poor


class Phone(Property):
    def __init__(self, name,  price, base, for_poor):
        super().__init__(name, price)
        self.for_poor = for_poor
        self.base = base


class Laptop(Property):
    def __init__(self, name,  price, reward, for_poor):
        super().__init__(name, price)
        self.reward = reward
        self.for_poor = for_poor


class Island(Property):
    def __init__(self, name,  price, reward, for_poor):
        super().__init__(name, price)
        self.reward = reward
        self.for_poor = for_poor


phone = Phone("Nokia 3310", 100, True, True)
laptop = Laptop("Siemens", 200, 1, True)
car = Car("Aveo", 1000, 5)

print(f"{phone.__dict__}\n")
print(laptop.__dict__)
print(car.__dict__)
