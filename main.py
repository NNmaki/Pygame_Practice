import pygame

pygame.init()
color = (255, 255, 255)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))
player2 = pygame.Rect((500, 350, 50, 50))
player3 = pygame.Rect((400, 300, 50, 50))
player4 = pygame.Rect((200, 200, 50, 50))

run = True
while run:

    screen.fill(color)

    # player on punainen - muutoksen jälkeen haalea pinkki
    pygame.draw.rect(screen, (255, 100, 100), player)

    # player2 on sininen
    pygame.draw.rect(screen, (0, 0, 255), player2)

    # player3 on vihrea
    pygame.draw.rect(screen, (0, 255, 0), player3)

    # player4 on musta
    pygame.draw.rect(screen, (0, 0, 0), player4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
