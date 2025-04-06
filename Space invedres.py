import pygame
import random
import math

screenwidth = 800
screenhight = 500
pstartx = 370
pstarty = 380
estartymin = 50
estartymax = 150
espeedx = 4
espeedy = 40
bspeedy = 10
cdistance = 27

pygame.init()
screen = pygame.display.set_mode((screenwidth, screenhight))
background = pygame.image.load('bg.webp')
pygame.display.set_caption('space invaders')
icon = pygame.image.load('ufo.webp')
pygame.display.set_icon(icon)

playimg = pygame.image.load('rocket.png')
playerx = pstartx
playery = pstarty
pxchange = 0

enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofe = 6

for _i in range(numofe):
    enemyimg.append(pygame.image.load('ufo.webp'))
    enemyx.append(random.randint(0, screenwidth - 64))
    enemyy.append(random.randint(estartymin, estartymax))
    enemyxchange.append(espeedx)
    enemyychange.append(espeedy)

bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = pstarty
bulletxchange = 0
bulletychange = bspeedy
bulletstate = "ready"

scorevalue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
overfont = pygame.font.Font('freesansbold.ttf', 64)

def showscore(x, y):
    score = font.render("Score:" + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameovertext():
    overtext = overfont.render("Game OVER!", True, (255, 255, 255))
    screen.blit(overtext, (200, 250))

def player(x, y):
    screen.blit(playimg, (x, y))

def enemey(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fireb(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x + 16, y + 20))

def isCollition(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx)**2 + (enemyy - bullety)**2)
    return distance < cdistance

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxchange = -5
            if event.key == pygame.K_RIGHT:
                pxchange = 5
            if event.key == pygame.K_SPACE and bulletstate == "ready":
                bulletx = playerx
                fireb(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pxchange = 0

    playerx += pxchange
    playerx = max(0, min(playerx, screenwidth - 64))

    for i in range(numofe):
        if enemyy[i] > 340:
            for j in range(numofe):
                enemyy[j] = 2000
            gameovertext()
            break

        enemyx[i] += enemyxchange[i]

        if enemyx[i] <= 0 or enemyx[i] >= screenwidth - 64:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]

        if isCollition(enemyx[i], enemyy[i], bulletx, bullety):
            bullety = pstarty
            bulletstate = "ready"
            scorevalue += 1
            enemyx[i] = random.randint(0, screenwidth - 64)
            enemyy[i] = random.randint(estartymin, estartymax)

        enemey(enemyx[i], enemyy[i], i)

    if bullety <= 0:
        bullety = pstarty
        bulletstate = "ready"

    if bulletstate == "fire":
        fireb(bulletx, bullety)
        bullety -= bulletychange

    player(playerx, playery)
    showscore(textx, texty)
    pygame.display.update()
