import pygame, random

# intialize the game 
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# title
pygame.display.set_caption("space invader")

playerimg = pygame.image.load('depth first search/spaceship.png')
playerX = 370
playerY = 480
x_change = 0


enemyimg = pygame.image.load('depth first search/alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyx_change = 0


def player(x,y):
    screen.blit(playerimg,((x,y)))

def enemy (x,y):
    screen.blit(enemyimg,((x,y)))



# Game LOOP
running = True 
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        # if keystroke is pressed check if right or left 
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.3
            if event.key == pygame.K_RIGHT:
                x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                x_change = 0
                
    playerX += x_change   
    if playerX <=0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768          
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()


