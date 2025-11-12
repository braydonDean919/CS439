import pygame
def image(screen):
    pygame.init()
    pygame.draw.rect(screen, (158, 100, 0), ((200, 175), (250, 400)), 300)#Body
    pygame.draw.rect(screen, (215, 169, 89), ((200, 10), (250, 250)), 300)#Head
    pygame.draw.rect(screen, "brown", ((260, 200), (125, 25)), 300)#Mouth
    pygame.draw.rect(screen, (0, 0, 0), ((300, 175), (50, 110)), 300)#Nose
    #arms
    pygame.draw.rect(screen, (0, 0, 0), ((140, 260), (60, 110)), 300)
    pygame.draw.rect(screen, (0, 0, 0), ((175, 310), (275, 60)), 300)
    pygame.draw.rect(screen, (0, 0, 0), ((450, 260), (60, 110)), 300)

    #Eyes
    pygame.draw.rect(screen, "white", ((375, 150), (25, 25)), 300)
    pygame.draw.rect(screen, "green", ((350, 150), (25, 25)), 300)
    pygame.draw.rect(screen, "green", ((275, 150), (25, 25)), 300)
    pygame.draw.rect(screen, "white", ((250, 150), (25, 25)), 300)
    pygame.draw.rect(screen, "black", ((250, 125), (150, 25)), 300)#Eye Brow

    #pygame.draw.line(screen, "black", (325,0),(325,480),1)Center Line X
   # pygame.draw.line(screen, "black", (0,237),(640,237),1)Center Line Y







def main():
    pygame.init()
    screen = pygame.display.set_mode((650, 475))
    screen.fill("white")
    pygame.display.set_caption("Drawing commands")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    image(background)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()




