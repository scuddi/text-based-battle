from character import Hero, Enemy
from weapons import short_bow, iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 100, weapons = short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    hero.drop()
    input()