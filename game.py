from os import system, name
import random 
from time import sleep

done = False

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.maxhealth = 20
        self.exp = 0
        self.level = 1
        self.damage = 0
        self.location = 1
        self.money = 99999999
        self.weapon = Weapon("Nothing",0,1)
        self.shield = Shield("Nothing",0,1)
        self.weapons = []
        self.shields = []
        self.potions = []
        self.addWeapon(self.weapon)
        self.addShield(self.shield)
        self.burned = False
        self.poisoned = False
    def getName(self):
        return self.name
    def getLocation(self):
        return self.location
    def getMoney(self):
        return self.money
    def getHealth(self):
        return self.health
    def getMaxHealth(self):
        return self.maxhealth
    def getLevel(self):
        return self.level
    def getWeapon(self):
        return self.weapon
    def getShield(self):
        return self.shield
    def getWeapons(self):
        lis = []
        for i in self.weapons:
            lis.append(i.getName())
        return lis
    def getAWeapon(self,index):
        return self.weapons[index]
    def getWeaponList(self):
        lis  = []
        x = 1
        for i in self.weapons:
            lis.append(str(x)+". "+i.getName()+" Damage: "+str(i.getDamage())+" Durability: "+str(i.getDurability()))
            x+=1
        return lis
    def getShields(self):
        lis = []
        for i in self.shields:
            lis.append(i.getName())
        return lis
    def getAShield(self,index):
        return self.shields[index]
    def getShieldList(self):
        lis  = []
        x = 1
        for i in self.shields:
            lis.append(str(x)+". "+i.getName()+" Protection: "+str(i.getProtection())+" Durability: "+str(i.getDurability()))
            x+=1
        return lis      
    def getPotions(self):
        lis = []
        for i in self.potions:
            lis.append(i.getName())
        return lis
    def getPotionList(self):
        lis  = []
        x = 1
        for i in self.potions:
            lis.append(str(x)+". "+i.getName())
            x+=1
        return lis
    def getAPotion(self, index):
        return self.potions[index]
    def usePotion(self, index):
        cur = self.getAPotion(index)
        eff = cur.getEffect()
        amt = cur.getAmt()
        if eff == 0: #0 is health, 1 is cure burn, 2 is cure poison, 3 is durability
            self.health += amt
            if self.health > self.maxhealth:
                self.health = self.maxhealth
        elif eff == 1:
            self.burned = False
        elif eff == 2:
            self.poisoned = False
        elif eff == 3:
            atDurPot(amt)
        self.potions.pop(index)
    def setWeapon(self,obj):
        self.weapon = obj
    def setShield(self, obj):
        self.shield = obj
    def setLocation(self,loc):
        self.location = loc
    def fullHeal(self):
        self.health = self.maxhealth
    def withdraw(self, obj, amt):
        amt = int(amt)
        self.money+=obj.withdraw(amt)
    def deposit(self, obj, amt):
        amt = int(amt)
        if self.money - amt <0:
            input("You do not have enough money")
            return 0
        else:
            self.money-= amt
            obj.deposit(amt)
    def addWeapon(self,obj):
        self.weapons.append(obj)
    def addShield(self, obj):
        self.shields.append(obj)
    def addPotion(self,obj):
        self.potions.append(obj)
    def buyWeapon(self, sword, amt):
        amt = int(amt)
        if self.money - amt < 0:
            input("You do not have enough money")
        else:
            self.money-=amt
            self.addWeapon(sword)
    def buyShield(self, shield, amt):
        amt = int(amt)
        if self.money - amt < 0:
            input("You do not have enough money")
        else:
            self.money-=amt
            self.addShield(shield)
    def buyPotion(self, potion, amt):
        amt = int(amt)
        if self.money - amt < 0:
            input("You do not have enough money")
        else:
            self.money-=amt
            self.addPotion(potion)

            
class Weapon:
    def __init__(self,name,damage,durability):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.maxdur = durability
    def getName(self):
        return self.name
    def getDamage(self):
        return self.damage
    def getDurability(self):
        return self.durability
    def fix(self, amt):
        self.durability += amt
        if self.durability > self.maxdur:
            self.durability = self.maxdur
        if amt == -1:
            self.durability == self.maxdur

class Shield:
    def __init__(self,name,protection,durability):
        self.name = name
        self.protection = protection
        self.durability = durability
        self.maxdur = durability
    def getName(self):
        return self.name
    def getProtection(self):
        return self.protection
    def getDurability(self):
        return self.durability
    def fix(self, amt):
        self.durability += amt
        if self.durability > self.maxdur:
            self.durability = self.maxdur
        if amt == -1:
            self.durability == self.maxdur

class Potion:
    def __init__(self, name, effect, amt):
        self.name = name
        self.effect = effect #0 is health, 1 is cure burn, 2 is cure poison, 3 is durability
        self.amt = amt
    def getName(self):
        return self.name
    def getEffect(self):
        return self.effect
    def getAmt(self):
        return self.amt

class Bank:
    def __init__(self):
        self.money = 20
    def withdraw(self, amt):
        amt = int(amt)
        if self.money - amt <0:
            input("You do not have enough money")
            return 0
        else:
            self.money-= amt
            return amt
    def deposit(self, amt):
        amt = int(amt)
        self.money+=amt
    def getMoney(self):
        return self.money
            

class Engine:
    def __init__():
        pass
    
    def run():
        pass

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def ask(prompt):
    answer = ""
    answer = input(prompt)
    while answer == "":
        answer = input("Please enter a response: ")
    return answer

def askint(prompt):
    answer = ask(prompt).strip()
    while checkint(answer) == False:
        answer = ask("Please enter an integer response: ").strip()
    return int(answer)

def checkint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def choose(options,prompt):
    for i in options:
        print(i)
    response = ask(prompt)
    try:
        response = response.strip()
        response = int(response)
    except:
        input("Enter a valid response ")
        choose(options,prompt)
    if int(response) <= len(options) and int(response)>0:
        return response
    else:
        input("Enter a valid response ")
        choose(options,prompt)

def randomStatement(options):
    length = len(options) - 1
    index = random.randint(0,length)
    input(options[index])
    
def numberify(group):
    x =1
    for i in group:
        i = str(x)+". "+str(i)
        x+=1
    

def callMap():
    menu = ["1. Home",
    "2. The Town",
    "3. The Cave",
    "4. The Forest"]
    response = int(choose(menu,"Where would you like to go?"))
    character.setLocation(response)
    atLocation()

def atLocation():
    loc = character.getLocation()
    if loc == 1: #Home
        randomStatement(["You are home","You are at your cottage","You are at your humble abode"])
        response = choose(["1. Sleep","2. See Chest", "3. Leave","4. See Inventory"], "What would you like to do?")
        if response == 1: #Sleep
            randomStatement(["You took a nap","You had a nice rest","You dreamed of nothing","You dreamed of your favorite meal","You dreamed of vanquishing all evil from the land"])
            print("Your health has been fully restored")
            input("Your current health is: "+str(character.getHealth()))
            character.fullHeal()
            atLocation()
        elif response == 2: #See Chest
            atChest()
        elif response == 3: #Leave
            callMap()
        elif response ==4: #Inventory
            atInventory()
            atLocation()
        else:
            input("That is not a valid response")
            atLocation()
    if loc == 2: #Town
        randomStatement(["You are in the town square","You are in the town"])
        response = choose(["1. Go To Shop","2. Go To Farm","3. Leave","4. See Inventory"],"What would you like to do? ")
        if response == 1: #Go to Shop
            atShop()
        elif response == 2:
            atFarm()
        elif response == 3:
            callMap()
        elif response == 4:
            atInventory()
            atLocation()
        

#Home defs
def atChest():
    input("You took a look at your chest")
    print("You have " + str(character.getMoney()) + " krollers on your person")
    input("You have " + str(chest.getMoney()) + " krollers in your chest")
    ans = choose(["1. Withdraw Money","2. Deposit Money", "3. Leave"],"What would you like to do? ")
    if ans == 1: #Withdraw
        amt = askint("How much do you want to withdraw?")
        character.withdraw(chest, amt)
        atChest()
    elif ans == 2: #Deposit
        amt = askint("How much do you want to deposit?")
        character.deposit(chest, amt)
        atChest()
    elif ans == 3: #Leave
        atLocation()
    else:
        input("That is not a valid response")
        atChest()
        
#Town defs
def atShop():
    randomStatement(["You are at the shop","You are in the shop"])
    ans = choose(["1. Weapons","2. Shields","3. Potions","4. Repair","5. Leave"],"What do you want to buy?")
    if ans == 1:
        atWeapons()
    elif ans == 2:
        atShields()
    elif ans == 3:
        atPotions()
    elif ans == 4:
        atRepair()
    elif ans == 5:
        atLocation()
    else:
        input("That is not a valid response")
        atShop()
#shop defs
def atWeapons():
    input("You have " + str(character.getMoney())+" krollers")
    resp = choose(["1. Wooden Sword: 20","2. Small Sword: 40","3. Knight's Sword: 100", "4. Leave", "5. See Inventory"],"Choose a sword")
    if resp == 1:
        character.buyWeapon(Weapon("Wooden Sword",5,20),20)
        atWeapons()
    elif resp == 2:
        character.buyWeapon(Weapon("Small Sword",10,40),40)
        atWeapons()
    elif resp == 3:
        character.buyWeapon(Weapon("Knight's Sword",25,200),100)
        atWeapons()
    elif resp == 4:
        atShop()
    elif resp == 5:
        atInventory()
        atWeapons()

def atShields():
    input("You have " + str(character.getMoney())+" krollers")
    resp = choose(["1. Wooden Shield: 15","2. Small Shield: 30","3. Knight's Shield: 80", "4. Leave", "5. See Inventory"],"Choose a shield")
    if resp == 1:
        character.buyShield(Shield("Wooden Shield",5,20),15)
        atShields()
    elif resp == 2:
        character.buyShield(Shield("Small Shield",5,20),30)
        atShields()
    elif resp == 3:
        character.buyShield(Shield("Knight's Shield",5,20),80)
        atShields()
    elif resp == 4:
        atShop()
    elif resp == 5:
        atInventory()
        atShields()

def atPotions():
    input("You have " + str(character.getMoney())+" krollers")
    resp = choose(["1. Small Potion, Heals 50: 10","2. Burn Potion, Cures Burns: 10","3. Poison Potion, Cures Poison: 10","4. Repair Potion, Repairs Swords and Shields: 40", "5. Leave", "6. See Inventory"],"Choose a sword")
    if resp == 1:
        character.buyPotion(Potion("Small Potion",0,50),10)
        atPotions()
    elif resp == 2:
        character.buyPotion(Potion("Burn Potion",1,1),10)
        atPotions()
    elif resp == 3:
        character.buyPotion(Potion("Poison Potion",2,1),10)
        atPotions()
    elif resp == 4:
        character.buyPotion(Potion("Repair Potion",3,100),40)
        atPotions()
    elif resp == 5:
        atShop()
    elif resp == 6:
        atInventory()
        atPotions()

def atRepair():
    ans = choose(["1. Weapons","2. Shields","3. Cancel"],"What would you like to repair?" )
    if ans == 1:
        resp = choose([list(character.getWeaponList()),str(len(character.getWeapons())+1)+". Leave"],"Choose which weapon to fix. Cost: 20. You have " + str(character.getMoney())+" krollers")
        if resp == len(character.getWeapons())+1:
            atInventory()
        character.getAWeapon(resp-1).fix(-1)
        atInventory()
    elif ans == 2:
        resp = choose([list(character.getShieldList()),str(len(character.getShields())+1)+". Leave"],"Choose which shield to fix. Cost: 20. You have " + str(character.getMoney())+" krollers")
        if resp == len(character.getShields())+1:
            atInventory()
        character.getAShield(resp-1).fix(-1)
        atInventory()
    elif ans == 3:
        atShop()
#Farm def
def atFarm():
    atLocation()

#Inventory
def atInventory():
    print(character.getName()+", Level "+str(character.getLevel())+", HP "+str(character.getHealth())+"/"+str(character.getMaxHealth()))
    print("Money: "+ str(character.getMoney()))
    print("Equipped Weapon: " + character.getWeapon().getName()+" Damage: "+ str(character.getWeapon().getDamage())+" Durability: "+ str(character.getWeapon().getDurability()))
    print("Equipped Shield: " + character.getShield().getName()+" Protection: "+ str(character.getShield().getProtection())+" Durability: "+ str(character.getShield().getDurability()))
    print("Weapons: "+str(character.getWeapons())[1:-1])
    print("Shields: "+str(character.getShields())[1:-1])
    input("Potions:"+str(character.getPotions())[1:-1])
    #menu for what to do
    ans = choose(["1. Equip Weapon","2. Equip Shield","3. Use Potion","4. Save Menu","5. Leave"],"What would you like to do? ")
    if ans == 1: #Equip Weapon
        resp = choose([list(character.getWeaponList()),str(len(character.getWeapons())+1)+". Leave"],"Choose which weapon to equip ")
        if resp == len(character.getWeapons())+1:
            atInventory()
        character.setWeapon(character.getAWeapon(resp-1))
        atInventory()
    if ans == 2: #Equip Shield
        resp = choose([list(character.getShieldList()),str(len(character.getShields())+1)+". Leave"],"Choose which shield to equip ")
        if resp == len(character.getShields())+1:
            atInventory()
        character.setShield(character.getAShield(resp-1))
        atInventory()
    if ans == 3: #Use Potion
        resp = choose([list(character.getPotionList()),str(len(character.getPotions())+1)+". Leave"],"Choose which potion to use ")
        if resp == len(character.getPotions())+1:
            atInventory()
        character.usePotion(resp-1)
        atInventory()
    if ans == 4: #Save
        atSave()
        atInventory()
    if ans == 5: #Leave
        pass
'''
        m, Level 1, HP 20/20
        Money: 99999949
        Equipped Weapon: Nothing Damage: 0 Durability: 1
        Equipped Shield: Nothing Protection: 0 Durability: 1
        Weapons: 'Nothing'
        Shields: 'Nothing'
        Potions:'Repair Potion'
      '''  
#potions
def atDurPot(amt):
    ans = choose(["1. Weapons","2. Shields","3. Cancel"],"What would you like to repair? Fixing Amount: "+str(amt))
    if ans == 1:
        resp = choose([list(character.getWeaponList()),str(len(character.getWeapons())+1)+". Leave"],"Choose which weapon to fix ")
        if resp == len(character.getWeapons())+1:
            atInventory()
        character.getAWeapon(resp-1).fix(amt)
        atInventory()
    elif ans == 2:
        resp = choose([list(character.getShieldList()),str(len(character.getShields())+1)+". Leave"],"Choose which shield to fix ")
        if resp == len(character.getShields())+1:
            atInventory()
        character.getAShield(resp-1).fix(amt)
        atInventory()
    elif ans == 3:
        pass


def atSave():
    resp = choose(["1. Save","2. Quit","3. Save and Quit","4. Back"],"What would you like to do?")
    if resp == 1: #save
        pass
    elif resp == 2: #quit
        asc = choose(["1. Yes","2. No"],"Are your sure? All unsaved data will be lost.")
        if asc == 1:
            exit()
        elif asc == 2:
            atSave()
    elif resp == 3: #save and quit
        pass
    elif resp == 4: #back
        pass
            
                            
        
            

chest = Bank()
input("Welcome to Praetoria")
new_name = ask("What is your name? ")
character = Player(new_name)
input("Nice to meet you, " + character.getName() + ".")
input("Today you are going to start your journey in this mystical land.")
atLocation()

while not done:
    pass
