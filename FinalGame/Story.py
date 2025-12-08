class Story:
    def __init__(self, events, characters):
        self.events = events
        self.characters = characters
        self.play_story()

    def play_story(self):
        for event in self.events:
            self.runEvent(event)

        

    def runEvent(self, event):
        event.toString()

        # Combat event
        if event.description == "attack":
            if len(event.characters) == 2:
                c1, c2 = event.characters
                print(f"{c1.name} launches an attack on {c2.name}!")
                self.doCombat(c1, c2)
            else:
                print("Invalid combat event — requires exactly 2 characters.")

       

        else:
            print(f"{event.description}")

    def doCombat(self, attacker, defender):
        from Combat import Combat
        fight = Combat(attacker, defender)
        
