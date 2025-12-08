class Combat:

    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def fight(char1,char2):
        keepGoing = True
        
        while keepGoing:
            enter = input("Press enter to fight... ")
            print("")
            char1.hit(char2)
            if char2.hitPoints <= 0:
                print(f"{char2.name} Died. {char1.name} Wins")
                keepGoing = False
            char2.hit(char1)
            if char1.hitPoints <=0:
                print(f"{char1.name} Died. {char2.name} Wins")
                keepGoing = False