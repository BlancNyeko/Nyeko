Classes = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
Races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Ork", "Halfling", "Human", "Tiefling"]
userInt = 0
counter = 0
valid = False
def RangeCheck(value,lBound,uBound):
    if value >= lBound and value <= uBound:
        return True
    else:
        return False

def RangeIntCheck(value,lBound,uBound):
    try :
        if int(value) >= lBound and int(value) <= uBound:
            return int(value)
        else:
            print("Ensure value is between " + str(lBound) + " and " + str(uBound))
            return 0
    except:
        print("Ensure the value is a number")
        return 0

class Character :

    def __init__(self, *args, **kwargs):
        self.name = ""
        self.race = ""
        self.background = ""
        self.charClass = ""
        self.Attributes = [0,0,0,0,0,0]
        self.hitDice = ""
        self.currentHP = 0
        self.maxHP = 0
        self.armorClass = 0
        self.valid = False

        
    def dosom(self):
        print("Hi")
    def getName(self) :
        print("Input Character Name")
        self.name = input()

    def getRace(self) :
        print("Choose your Race.")  
        counter = 1
        for x in Races:
            
            print(str(counter) + "." + x)
            counter = counter + 1

        
        userInt = 0
        while userInt == 0:
            userInt = RangeIntCheck(input(), 1, len(Races))

        self.race = Races[userInt - 1]

    def getClass(self) :
        print("Choose your Race.")
        counter = 1
        for x in Classes:
            print(str(counter) + "." + x)
            counter = counter + 1
        userInt = 0

        while userInt == 0:
            userInt = RangeIntCheck(input(), 1, len(Classes))
        self.charClass = Classes[userInt - 1]

a1 = Character()
a1.getName()
a1.getRace()
a1.getClass()

print(a1.name + a1.charClass + a1.race)

