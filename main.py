from character import Hero, Enemy
from weapons import short_bow

hero = Hero(name = "Hero", health = 100)
enemy = Enemy(name = "Enemy", health = 100, weapons = short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Healt of {enemy.name}: {enemy.health}")

    input()