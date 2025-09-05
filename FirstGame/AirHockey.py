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

class Paddle(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("Paddle.png")
        self.setSize(100,100)
        self.setAngle(90)
        self.x = self.screenWidth/2

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        
        self.puck = Puck(self)
        self.paddleTop = Paddle(self)
        self.paddleTop.y = 50
        self.paddleBottom = Paddle(self)
        self.paddleBottom.y = 425
        self.moveSpeed = 4
        self.sprites = [self.puck, self.paddleBottom,self.paddleTop]
    def process(self):
        
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
        

def main():
    game = Game()
    game.start()
if __name__ == "__main__":
    main()

