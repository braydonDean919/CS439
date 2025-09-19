

def loadGame():
    game = {
"start":	["You decide to go fishing select your bait.","Worms",	"worms","Artificial",	"artificial"],
"worms":	["Okay, you Chose worms, what type of pole will you use?","Strong Pole","strWorm","Lite Pole","liteWorm"],
"strWorm":	["Good choice, You cast and reel in a Massive Catfish.",	"Keep as a trophy",	"keep",	"Switch Bait",	"artificial"],
"liteWorm":	["Bad Choice, your lite pole broke the fish was too big.",	"Switch Pole", 	"strWorm",	"Switch Bait",	"artificial"],
"artificial":["You chose the artificial bait what kind of pole would you like?"	,"Strong Pole","strArt","Lite Pole"	,"liteArt"],
"strArt":	["You overwork yourself from reeling so much with a big pole and you have a heart attck and die.",	"Start over",	"start",	"Quit",	"quit"],
"liteArt":	["Congrulations you reeled in a world record Bass!!!",	"Keep as a trophy",	"keep",	"Release and keep fishing",	"release"],
"keep":	["You became a legend and decided to permitly retire from fishing.",	"Start over???",	"start","Quit",	"quit"],
"release":	["You gained some honor in the eyes of the fish...Humans called you stuiped so you kept fishing.","Worms" ,"worms",	"Artificial","artificial"]
    }
    return game
def playNode(node, game):
    [description, choiceA, nodeA, choiceB, nodeB]  = game[node]
    print(f"""{description} 
         
          1. {choiceA}
          
          2. {choiceB}
          
          """)
    userChoice = input("What will you do? HINT: Pick 1 or 2 ")
    print("")
    if userChoice == "1":
        choice = nodeA
    elif userChoice == "2":
        choice = nodeB
    else:
        print("YOU HAD ONE JOB 1 OR 2 THAT'S IT there is nothing else!!!")
        choice = node
    return(choice)
def main():
    game = loadGame()
    currentNode = "start"
    keepGoing = True
    while(keepGoing):
        currentNode = playNode(currentNode, game)
        if currentNode == "quit":
            keepGoing = False

if __name__ == "__main__":
    main()