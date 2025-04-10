# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} with my power: {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Derived class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!")

# Example usage
hero1 = Superhero("ShadowStrike", "Invisibility", "Neon City")
hero2 = FlyingHero("SkyBlazer", "Wind Control", "Cloud Haven", 800)

hero1.introduce()
hero1.use_power()
print()
hero2.introduce()
hero2.use_power()
