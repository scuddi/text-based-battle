class Weapon:
    def __init__(self, name: str, type: str, damage: int, value: int):
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value

iron_sword = Weapon(name = "Iron Sword",
                    type = "sharp",
                    damage = 5,
                    value = 10)

short_bow = Weapon(name = "Short Bow",
                   type = "range",
                   damage = 4,
                   value = 8)

fists = Weapon(name = "Fists",
               type = "blunt",
               damage = 2,
               value = 0)