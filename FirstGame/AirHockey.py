import simpleGE, pygame, random
class Intro(simpleGE.Scene):
    def __init__(self,fScore = 0,sScore = 0):
        super().__init__()
        self.status = "quit"
        self.fScore =fScore
        self.sScore = sScore
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "To begin press the space key",
            "Top player's controls are wasd",
            "Bottom player's controls are the arrow keys",
            "First to 10 points wins",
            "Press Q to quit"]
        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (450, 200)
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 100)
        self.lblScore.size = (400, 30)
        self.lblScore.text = f"Previous Score: {self.fScore} : {self.sScore}"
        self.sprites = [self.lblInstructions,self.lblScore]
    def process(self):
        if self.isKeyPressed(pygame.K_q):
            self.status = "quit"
            self.stop()
        elif self.isKeyPressed(pygame.K_SPACE):
            self.status = "play"
            self.stop()
class Nets(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setSize(200, 1)
        self.x = self.screenWidth/2
class Puck(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Puck.png")
        self.setSize(50,50)
        self.boundAction = self.BOUNCE
        self.x = self.screenWidth/2
        self.y = self.screenHeight/2
        self.setAngle((random.randint(0, 360)))
        self.dx = 1
        self.dy = 1
    def reset(self):
        self.x = self.screenWidth/2
        self.y = self.screenHeight/2
        self.setAngle((random.randint(0, 360)))
        self.dx = random.randint(-5,5)
        self.dy = random.randint(-5,5)

        

class Paddle(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("Paddle.png")
        self.setSize(100,100)
        self.setAngle(90)
        self.x = self.screenWidth/2
        self.boundAction = self.STOP
class Scorelbl(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (70, 20)
        self.text = "Top : Bottom"
        


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.puck = Puck(self)
        self.paddleTop = Paddle(self)
        self.paddleTop.y = 50
        self.netTop = Nets(self)
        self.netTop.y = 2
        self.paddleBottom = Paddle(self)
        self.paddleBottom.y = 425
        self.netBottom = Nets(self)
        self.netBottom.y = 478
        self.moveSpeed = 4
        self.topScore = 0
        self.bottomScore = 0
        self.scoreLbl = Scorelbl()
        self.sprites = [self.puck, self.paddleBottom,self.paddleTop,self.netBottom,self.netTop,self.scoreLbl]
    def process(self):
        maxDY = 5
        self.scoreLbl.text = f"{self.topScore} : {self.bottomScore}"
        if self.isKeyPressed(pygame.K_d):   
            self.paddleTop.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_a):   
            self.paddleTop.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_w):   
            self.paddleTop.forward(5)
        if self.isKeyPressed(pygame.K_s):   
            self.paddleTop.forward(-5)
        if self.isKeyPressed(pygame.K_RIGHT):
            self.paddleBottom.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.paddleBottom.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.paddleBottom.forward(-5)
        if self.isKeyPressed(pygame.K_UP):
            self.paddleBottom.forward(5)
        if self.puck.collidesWith(self.paddleBottom):
            self.puck.dx *= -1
            relY = self.puck.y - self.paddleBottom.y
            relY /= self.paddleBottom.rect.height
            relY *= 2
            relY *=maxDY
            self.puck.dy = relY
        if self.puck.collidesWith(self.paddleTop):
            self.puck.dx *= -1
            relY = self.puck.y - self.paddleTop.y
            relY /= self.paddleBottom.distanceTo(self.puck.)
            relY *= 2
            relY *=maxDY
            self.puck.dy = relY
        if self.puck.collidesWith(self.netBottom):
            self.puck.reset()
            self.topScore +=1
        if self.puck.collidesWith(self.netTop):
            self.puck.reset()
            self.bottomScore +=1
        if self.isKeyPressed(pygame.K_r):
            self.puck.reset()
        if self.topScore == 10:
            self.stop()
        if self.bottomScore == 10:
            self.stop()

def main():
    keepGoing = True    
    fScore =0 
    sScore = 0
    while keepGoing:
        intro = Intro(fScore,sScore)
        intro.start()
        if intro.status == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
            fScore = game.topScore
            sScore = game.bottomScore
            
if __name__ == "__main__":
    main()

