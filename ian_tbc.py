# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:03:24 2024

@author: ikowa
"""
import random
class Character(object):
    def __init__(self,name= "george", hitpoints = 20, hitChance = 50, maxDamage = 3, armor = 1):
        super().__init__()
        self.name = name
        self.hitpoints = hitpoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
       	self.__name = value
    @property
    def hitpoints(self):
         return self.__hitpoints
    @hitpoints.setter
    def hitpoints(self,value):
       	self.__hitpoints = value

    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
    
    def printStats(self):
        print(f"""
{self.name}
    Hit points: {self.hitpoints}
    Hit Chance: {self.hitChance}
    Max Damage: {self.maxDamage}
    Armor: {self.armor}
              """)

def hitChance(self, monster):
    playerHit = random.randint(0, 100)
    #print("help")
    if int(playerHit) <= self.hitChance:
        print(f"{self.name}'s battle hammer makes contact with {monster.name} ...")
        playerDam = random.randint(0, self.maxDamage)
        finalDam = int(playerDam) - int(monster.armor)
        if int(finalDam) < 0:
            finalDam = 0
        if monster.armor > 0:
            print(f"but {monster.name}'s armor deflects {monster.armor} points of damage")
        print(f"for {finalDam} points of damage")
        #print(finalDam)
        monster.hitpoints -= int(finalDam)
        print(f"{monster.name} has {monster.hitpoints} health \n") 
        #print(f"{finalDam} final dam")
        #rint({"monster.hitpoints"})
    else:
        print(f"{self.name} misses {monster.name}")

        
    # need to check if damage s positive, so I can end if they die

def main(hero,monster):
        
       hero = Character()
       hero.name =  "George bob"
       monster = Character()
       monster.name = "Monster"
       #monster = Character("",40, 30, 3, 2)
       
       hero.printStats()
       monster.printStats()
       hitChance(hero,monster)
       hitChance(monster,hero)

if __name__ == "__main__":
       main("hero","monster")
       