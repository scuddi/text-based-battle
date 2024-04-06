from weapons import fists
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapons = fists

    def attack(self, target):
        target.health -= self.weapons.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapons.damage} damage to {target.name} with {self.weapons.name}")

class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name=name, health = health)

        self.default_weapon = self.weapons
        self.health_bar = HealthBar(self, color="purple")

    def equip(self, weapons):
        self.weapons = weapons
        print(f"{self.name} equipped a(n) {self.weapons.name}!")

    def drop(self):
        self.weapons = self.default_weapon
        print(f"{self.name} dropped {self.weapons.name}")


class Enemy(Character):
    def __init__(self, name: str, health: int, weapons):
        super().__init__(name=name, health = health)
        self.weapons = weapons

        self.health_bar = HealthBar(self, color = "red")

