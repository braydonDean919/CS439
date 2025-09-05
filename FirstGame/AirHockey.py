import simpleGE, pygame, random
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
        self.rest
        self.setAngle((random.randint(0, 360)))
        self.dx = 5
        self.dy = 5
    def rest(self):
        self.x = self.screenWidth/2
        self.y = self.screenHeight/2

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
            relY /= self.paddleBottom.rect.height
            relY *= 2
            relY *=maxDY
            self.puck.dy = relY
        if self.puck.collidesWith(self.netBottom):
            self.puck.rest()
            self.topScore +=1
        if self.puck.collidesWith(self.netTop):
            self.puck.rest()
            self.bottomScore +=1




def main():
    game = Game()
    game.start()
if __name__ == "__main__":
    main()

