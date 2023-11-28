import pygame
import os
import random
import math
from pygame import mixer


# initialize the pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600)) # width and height


# BackGround
background = pygame.image.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/background.png')


# BackGround Sound
mixer.music.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/space_ship.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/player.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7
for enemies in range(num_of_enemies):
    enemyImg.append(pygame.image.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/enemy2.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)


# Bullet
bulletImg = pygame.image.load('zzz_projetos/freeCodeCamp/SPACE_INVADERS/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving


# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10


# Game over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score -> " + str(score_value), True, (255, 255,  255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255,  255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isColission(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



# Game Loop
running = True
while running:

    # RGB - Red Green Blue
    screen.fill((0, 0, 0))

    # BackGround image
    screen.blit(background, (0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            os.sys.exit()
        
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('zzz_projetos/freeCodeCamp/SPACE_INVADERS/laser.wav')
                    bullet_Sound.play()
                    # Get the current x cordenate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Cheking for boundaries of spaceship so it doesn't go out of bouds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for J in range(num_of_enemies):
                enemyY[J] = 2000
            
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0: # touch on the corner left
            enemyX_change[i] = 5 # change the direction x
            enemyY[i] += enemyY_change[i] # go a little for down (axis y)
        elif enemyX[i] >= 736: # touch on the corner right
            enemyX_change[i] = -5 # change the direction x
            enemyY[i] += enemyY_change[i] # go a little for down (axis y)
        
        # Colission
        colission = isColission(enemyX[i], enemyY[i], bulletX, bulletY)
        if colission:
            colission_Sound = mixer.Sound('zzz_projetos/freeCodeCamp/SPACE_INVADERS/explosion.wav')
            colission_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 
    


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()