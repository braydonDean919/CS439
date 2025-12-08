import random
class Character(object):
    def __init__(self, name = "Default", hitPoints = 0,hitChance = 0, maxDamage = 0, armor = 0, mana = 0, knowledge = 0, manaRecovery = 0, manaDamage = 0, recover = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        self.mana = mana
        self.knowledge = knowledge
        self.recover = recover
        self.manaRecovery = manaRecovery
        self.manaDamage = manaDamage
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def hitPoints (self):
        return self.__hitPoints
    @hitPoints.setter
    def hitPoints(self,value):
        if type(value) == int:
            if value >= 0:
                self.__hitPoints = value
            else:
                self.__hitPoints = 0

        else:
            print("Hit Points must be a number")
            self.__hitPoints = 1
    
    @property 
    def maxDamage (self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage (self, value):
        if type(value) == int:
            if value >= 0:
                self.__maxDamage = value
            else:
                print("max damage must be positive")
                self.__maxDamage = 1

        else:
            print("Max Damage must be a number")
            self.__maxDamage = 1
    @property
    def armor(self):
       return self.__armor
    @armor.setter
    def armor(self, value):
       if type(value) == int:
           if value >= 0:
               self.__armor = value
           else:
               print("Armor must be positive")
               self.__armor = 1

       else:
           print("Armor must be a number")
           self.__armor = 1
    @property
    def hitChance(self):
         return self.__hitChance
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    self.__hitChance = value
                else:
                    print("Hit Chance must be less than or euqal to 100")
                    self.__hitChance = 100
            else:
                print("Hit Chance must be positive")
                self.__hitChance = 1

        else:
            print("Hit Chance must be a number")
            self.__hitChance = 1
    @property 
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self, value):
        if type(value) == int:
            if value >= 0:
                self.__mana = value
            else:
                print("Mana must be positive")
                self.mana = 1
        else:
            print("Mana must be an Integer")
            self.mana = 1
    @property
    def knowledge(self):
        return self.__knowledge
    @knowledge.setter
    def knowledge(self, value):
        if type(value) == int:
            if value >= 0:
                self.__knowledge = value
            else:
                print("Knowledge must be positive")
                self.__knowledge = 1
        else:
            print("Knowledge must be an Integer")
            self.__knowledge = 1
            
    @property
    def manaRecovery(self):
        return self.__manaRecovery
    @manaRecovery.setter
    def manaRecovery(self, value):
        if type(value) == int:
            if value >= 0:
                self.__manaRecovery = value
            else:
                print("Mana Recovery must be positive")
                self.__manaRecovery = 1
        else:
            print("Mana Recovery must be an Integer")
            self.__manaRecovery = 1
    @property        
    def recover(self):
        return self.__recover
    @recover.setter
    def recover(self, value):
        if type(value) == int:
            if value >= 0:
                self.__recover = value
            else:
                print("Recovery must be positive")
                self.__recover = 1
        else:
            print("Recovery must be an Integer")
            self.__recover = 1
            
    @property        
    def manaDamage(self):
        return self.__manaDamage
    @manaDamage.setter
    def manaDamage(self, value):
        keepGoing = True
        while(keepGoing):
            if type(value) == int:
                if value >= 0:
                    self.__manaDamage = value
                    keepGoing = False
                else:
                    print("Mana Damage must be positive") 
            else:
                print("Mana Damage must be an Integer") 
    def heal(self):
        
        self.hitPoints += self.recover
        print(f"You recoverd {self.recover} HP so you know have {self.hitPoints}")
        self.mana -= 10
        
    def hit(self,character2):
        chance = random.randint(0,100)
        if self.hitChance >= chance:
            damage = random.randint(1,self.maxDamage)
            print(f"{self.name} hit {character2.name} for {damage} points of damage ")
            print("")
            if character2.armor > 0:
                if damage > character2.armor:
                    remain = damage - character2.armor
                    print(f"{character2.name}'s armor absorbed {character2.armor} points of damage\n")
                else:
                    print(f"{character2.name}'s armor absorbed all of the damage \n")
                    remain = 0
            else:
                remain = damage
            if remain >= 0:
                character2.hitPoints = character2.hitPoints - remain
                print(f"{character2.name} has {character2.hitPoints} hp left\n")
        else:
            print(f"{self.name} missed\n")
    def manaAttack(self,enemy):
        self.mana -= 10
        chance = random.randint(0,100)
        if self.knowledge >= chance:
            print(f"{self.name} used fireball for {self.manaDamage} points of damage\n")
            enemy.hitPoints -= self.manaDamage 
            print(f"{enemy.name} has {enemy.hitPoints} hp left\n")
        else:
            print("Fireball missed it's target")
    def fight(self, enemy):
            attack = random.randint(1,3)
            enInput = str(attack)
            if enInput == "1":
                self.hit(enemy)
            elif enInput == "2":
                if self.mana >= 20:
                    self.manaAttack(enemy)
                else:
                    print("You don't have enough mana so you use a basic attack")
            elif enInput == "3":
                if self.mana >= 10:
                    self.heal(self)
                else:
                    print("You don't have enough mana so you use a basic attack")
            else:
                print("Please input a number from 1 to 3")
            self.mana += self.manaRecovery
            print(f"You now have {self.mana} Mp")
            enemy.hit(self)
            if self.hitPoints <= 0:
                print(f"You have Died. {enemy.name} Wins")
                keepGoing = False
            if enemy.hitPoints <=0:
                print(f"{enemy.name} Died. You Win")
                keepGoing = False

    def printStats(self):
        print(f"""
{self.__name}
_______________
HP - {self.hitPoints}
Mana - {self.mana}
Hit Chance - {self.hitChance}
Max Damage - {self.maxDamage}
Armor - {self.armor}
Knowledge - {self.knowledge}
Mana Recovery Rate - {self.manaRecovery} 
_______________
Skills
_______________
Healing Spell - Heal {self.recover} points
Fireball - Deal {self.manaDamage} ammount of damage avoiding armor
              """)
    def toDict(self):
        return {
            "name": self.name,
            "hitPoints": self.hitPoints,
            "hitChance": self.hitChance,
            "maxDamage": self.maxDamage,
            "armor": self.armor,
            "mana": self.mana,
            "knowledge": self.knowledge,
            "manaRecovery": self.manaRecovery,
            "manaDamage": self.manaDamage,
            "recover": self.recover,
        }