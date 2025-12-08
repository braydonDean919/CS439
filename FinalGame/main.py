import  Character, Story,Event, Enemy, json
def saveGame(characters, events, filename="saveFile.json"):
	
	#Saves all characters, events, and to a JSON save file.
	data = {
		"characters": [c.toDict() for c in characters],
		"events": [e.toDict() for e in events],
	}
	
	with open(filename, "w") as f:
		json.dump(data, f, indent=4)
	
	print("\nGame saved successfully!")

def loadGame(filename="saveFile.json"):
	#Loads characters and events back from the save file.
	
	try:
		with open(filename, "r") as f:
			data = json.load(f)
	except FileNotFoundError:
		print("No save file found.")
		return [], [], []

	# Load Characters
	characters = []
	for c in data["characters"]:
		char = Character.Character(
			c["name"],
			c["hitPoints"],
			c["hitChance"],
			c["maxDamage"],
			c["armor"],
			c["mana"],
			c["knowledge"],
			c["manaRecovery"],
			c["manaDamage"],
			c["recover"],
		)
		characters.append(char)

	# Load Events
	events = []
	for e in data["events"]:
		charsInvolved = [ch for ch in characters if ch.name in e["characters"]]
		event = Event.Event(e["title"], e["description"], charsInvolved)
		events.append(event)


	print("Game loaded successfully!")
	return characters, events

def createEvent(characters):
    title = input("Event title: ")
    description = ""
    print("\nSelect characters involved (enter numbers separated by commas):")
    for i, c in enumerate(characters):
        print(f"{i+1}. {c.name}")
    choices = input("Characters: ").replace(" ", "").split(",")
    chosenCharacters = []
    for ch in choices:
        if ch.isdigit():
            index = int(ch) - 1
            if 0 <= index < len(characters):#Checks to make sure the characters aren't empty
                chosenCharacters.append(characters[index])
    attack = input("Do the characters attack each other?y/n: ")
    if attack == "y":
        if len(chosenCharacters) == 2:
           description = "attack"
        elif len(chosenCharacters) > 2:
           print("Too many characters")
        else:
            print("Not enough characters")
    elif attack == "n":
            description = input("What happens?")

        
    return Event.Event(title, description, chosenCharacters)



def main():
    characters = []
    events = []
    print("--- RPG Creator ---")

    keepGoing =True
    while keepGoing:
        command = input("""
What would you like to do? Pick a Number
    1. Make a Character
    2. Make a new Event
    3. Make an Enemy
    4. Play the Game
    5. Save the Game
    6. Load Game
    7. Quit\n""")
        if command == "1":#Build the character the way the user wants
            name = input("Name: ")
            hp = int(input("Hit Points: "))
            hit = int(input("Hit Chance (0-100): "))
            dmg = int(input("Max Damage: "))
            armor = int(input("Armor: "))
            mana = int(input("Mana: "))
            knowledge = int(input("Knowledge: "))
            manaRecovery = int(input("Mana Recovery: "))
            manaDamage = int(input("Mana Damage: "))
            recover = int(input("Recovery Speed: "))
            char = Character.Character(name, hp, hit, dmg, armor,mana, knowledge, manaRecovery, manaDamage,recover)
            characters.append(char)
        
        if command == "2":
            if len(characters) == 0:
                print("You need at least one character to make events.")
            else:
                events.append(createEvent(characters))
        
        if command == "3":
            name = input("Name: ")
            hp = int(input("Hit Points: "))
            hit = int(input("Hit Chance (0-100): "))
            dmg = int(input("Max Damage: "))
            armor = int(input("Armor: "))
            mana = int(input("Mana: "))
            knowledge = int(input("Knowledge: "))
            manaRecovery = int(input("Mana Recovery: "))
            manaDamage = int(input("Mana Damage: "))
            recover = int(input("Recovery Speed: "))
            enemy = Enemy.Character(name, hp, hit, dmg, armor,mana, knowledge, manaRecovery, manaDamage,recover)
            characters.append(enemy)
        if command == "4":
            if len(events) > 0:
                Story.Story(events,characters)
            else:
                print("\nNo events were created — no story to show.")
        if command == "5":
             saveGame(characters,events)
        if command == "6":
            characters, events =loadGame()
        if command == "7":
             keepGoing = False

    # Play the game
   

if __name__ == "__main__":
    main()