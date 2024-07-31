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

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    key2 = pygame.key.get_pressed()
    if key2[pygame.K_f] == True:
        player2.move_ip(-2,0)
    elif key2[pygame.K_h] == True:
        player2.move_ip(2,0)
    elif key2[pygame.K_t] == True:
        player2.move_ip(0,-2)
    elif key2[pygame.K_g] == True:
        player2.move_ip(0,2)

    key3 = pygame.key.get_pressed()
    if key3[pygame.K_a] == True:
        player3.move_ip(-1,0)
    elif key3[pygame.K_d] == True:
        player3.move_ip(1,0)
    elif key3[pygame.K_w] == True:
        player3.move_ip(0,-1)
    elif key3[pygame.K_s] == True:
        player3.move_ip(0,1)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
