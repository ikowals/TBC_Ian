# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:49:46 2024

@author: ikowa
"""

import ian_tbc

def main():
    
    hero = ian_tbc.Character()
    hero.name = "George lopez"
    hero.hitpoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = ian_tbc.Character("Society", 20, 30, 5, 0)
    monster = ian_tbc.Character()
    monster.name = "George lopez"
    monster.hitpoints = 10
    monster.hitChance = 50
    monster.maxDamage = 5
    monster.armor = 2
    
    #hero.printStats()
    #monster.printStats()
    
    
    keepGoing = True
    while keepGoing:
       
        ian_tbc.main(hero,monster)
    
        #ian_tbc.main(monster,hero)
        if monster.hitpoints <= 0:
            print(f"{monster.name} has died")
            keepGoing = False
        elif hero.hitpoints <= 0:
            print(f"{hero.name} has died")
            keepGoing = False
            print("game over")

if __name__ == "__main__":
    main()