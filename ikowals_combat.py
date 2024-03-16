# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:49:46 2024

@author: ikowa
"""

import ian_tbc

def main():
    
    hero = ian_tbc.Character()
    hero.name = "Grand Hero"
    hero.hitpoints = 10
    hero.hitChance = 5
    hero.maxDamage = 5
    hero.armor = 2

    monster = ian_tbc.Character("Society", 20, 30, 5, 0)
    monster = ian_tbc.Character()
    monster.name = "The Terrible Monster"
    monster.hitpoints = 15
    monster.hitChance = 30
    monster.maxDamage = 2
    monster.armor = 1
    
    #hero.printStats()
    #monster.printStats()
    
    
    keepGoing = True
    while keepGoing:
        ian_tbc.hitChance(hero, monster)
        ian_tbc.hitChance(monster, hero)
        input("Press enter to continue")
        if monster.hitpoints <= 0:
            print(f"{monster.name} has died")
            keepGoing = False
        elif hero.hitpoints <= 0:
            print(f"{hero.name} has died")
            keepGoing = False
            print("game over")

if __name__ == "__main__":
    main()