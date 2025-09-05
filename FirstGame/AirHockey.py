import simpleGE, pygame, random

class Puck(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Puck.png")
        self.setSize(50,50)
        self.boundAction = self.BOUNCE
        self.x = self.screenWidth/2
        self.y = self.screenHeight/2
        self.setAngle((random.randint(0, 360)))
        self.dx = 5
        self.dy = 5



class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.puck = Puck(self)
        self.sprites = [self.puck]

def main():
    keepGoing = True
    while keepGoing:
       game = Game()
       game.start()
if __name__ == "__main__":
    main()

